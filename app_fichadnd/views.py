import uuid
import logging
import requests
import random
import re
import unicodedata
import logging
import pprint
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from app_fichadnd.logging import SafeRequestFormatter
from app_fichadnd.utils.complements import (
    TRANSLATIONS,
    SKILLS_MAP,
    RESIST_MAP,
    gen_atributos,
    XP_BY_LEVEL,
    proficiency_by_level,
    MOD_TABLE,
    LANGUAGES,
)
from app_fichadnd.utils.backgrounds import backgrounds
from app_fichadnd.utils.subraces import subraces


logger = logging.getLogger('app_fichadnd.views')
API_BASE = "https://www.dnd5eapi.co/api/2014"



class RequestLoggerAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        extra = self.extra.copy()
        if 'extra' in kwargs:
            combined = extra.copy()
            combined.update(kwargs['extra'])
            kwargs['extra'] = combined
        else:
            kwargs['extra'] = extra
        return msg, kwargs

def normalize_slug(text):
    text = unicodedata.normalize('NFKD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c))
    text = re.sub(r'[^\w\s-]', '', text)
    return text.strip().lower().replace(' ', '-')

def get_adapter(request, view_name: str):
    request_id = uuid.uuid4().hex
    user_ip = request.META.get('REMOTE_ADDR', '')
    return RequestLoggerAdapter(logger, {
        'request_id': request_id,
        'view': view_name,
        'user_ip': user_ip
    })

@require_http_methods(['GET'])
def home(request):
    adapter = get_adapter(request, 'home')
    lang = request.GET.get('lang', 'pt')
    adapter.debug('Acessando home', extra={'lang': lang})
    return render(request, 'pages/home.html', {'current_lang': lang})

def pick_starting_equipment_options(options_list):
    picks = []

    for opt in options_list:
        choose_n = opt.get("choose", 0)
        from_block = opt.get("from", {})

        if from_block.get("option_set_type") == "options_array":
            pool = []
            for entry in from_block.get("options", []):
                if "count" in entry and "of" in entry:
                    name = entry["of"]["name"]
                    qty  = entry.get("count", 1)
                    pool.append(f"{qty}× {name}")
                elif "item" in entry:
                    pool.append(entry["item"]["name"])
            k = min(choose_n, len(pool))
            if k > 0:
                picks += random.sample(pool, k=k)

        elif from_block.get("option_set_type") == "equipment_category":
            cat_url = from_block["equipment_category"]["url"]
            try:
                resp = requests.get(API_BASE + cat_url)
                resp.raise_for_status()
                data = resp.json()
            except requests.exceptions.HTTPError:
                continue
            except Exception:
                continue

            names = [e["name"] for e in data.get("equipment", [])]
            k = min(choose_n, len(names))
            if k > 0:
                picks += random.sample(names, k=k)

        else:
            desc = opt.get("desc", "(sem descrição)")
            picks.append(f"{desc} (não tratado automaticamente)")

    return picks

@require_http_methods(['GET', 'POST'])
def criando(request):
    adapter = get_adapter(request, 'criando')

    if request.method == 'GET':
        prev = request.session.get('ultima_ficha')
        if not prev:
            adapter.warning('Nenhuma ficha em sessão; redirecionando para home.')
            return redirect(reverse('home'))
        lang = request.GET.get('lang', prev.get('lang', 'pt'))
        prev['translations'] = {k: v[lang] for k, v in TRANSLATIONS.items()}
        adapter.debug('Preview via GET', extra={'lang': lang})
        return render(request, 'pages/criando.html', prev)

    data = request.POST.dict()
    adapter.debug('POST keys recebidas', extra={'keys': list(data.keys())})
    adapter.info('Recebendo POST para criar ficha', extra=data)

    lang = request.GET.get('lang', 'pt')
    translations = {k: v[lang] for k, v in TRANSLATIONS.items()}
    nome       = data.get('charname', '')
    classe     = data.get('classe', '')
    subclasse  = data.get('subclasse', '')
    classlevel = data.get('classlevel', '')
    background_slug = normalize_slug(request.POST.get('antecedente', ''))
    playername = data.get('playername', '')
    race       = data.get('race', '')
    subraca    = data.get('subrace', '')
    alinhamento= data.get('alignment', '')
    experience = data.get('experiencepoints', '')
    adapter.debug('Campos básicos', extra={
        'charname': nome, 'classe': classe, 'subclasse': subclasse,
        'classlevel': classlevel, 'background': background_slug,
        'playername': playername, 'race': race, 'subrace': subraca,
        'alinhamento': alinhamento, 'experience': experience,
    })

    ATTR_KEYS = ['strength','dexterity','constitution','intelligence','wisdom','charisma']
    atributos = {k: gen_atributos() for k in ATTR_KEYS}
    adapter.info(f'Atributos gerados aleatoriamente {atributos}')
    ABBRS = ['str','dex','con','int','wis','cha']
    modificadores = {abbr: MOD_TABLE.get(atributos[key], 0) for abbr, key in zip(ABBRS, ATTR_KEYS)}
    adapter.debug('Atributos iniciais e modificadores', extra={'atributos': atributos, 'modificadores': modificadores})

    class_slug   = classlevel.split()[0].lower() if classlevel else ''
    race_slug    = race.lower().replace(' ', '-')
    subrace_slug = subraca.lower().replace(' ', '-') if subraca else ''
    adapter.debug('Slugs gerados', extra={'class_slug': class_slug, 'race_slug': race_slug, 'subrace_slug': subrace_slug})

    background_data = backgrounds.get(background_slug, {})

    background_skills = [
    prof['name'] for prof in background_data.get('skill_proficiencies', [])
    ]

    api_base = 'https://www.dnd5eapi.co/api'
    race_data = {}
    try:
        resp = requests.get(f'{api_base}/races/{race_slug}')
        resp.raise_for_status()
        race_data = resp.json()
        speed = race_data.get('speed')
        adapter.debug('Dados da raça obtidos', extra={'race': race_data.get('name')})
    except Exception:
        adapter.exception('Erro buscar raça', extra={'race_slug': race_slug})

    class_data = {}
    try:
        resp = requests.get(f'{api_base}/classes/{classe}')
        resp.raise_for_status()
        class_data = resp.json()
        adapter.debug('Dados da classe obtidos', extra={'class': classe})
    except Exception:
        adapter.exception('Erro buscar classe', extra={'classe': classe})

    get_local_subrace = subraces.get(subrace_slug, {})

    subrace_data = {}
    if subrace_slug:
        try:
            resp = requests.get(f'{api_base}/subraces/{subrace_slug}')
            resp.raise_for_status()
            subrace_data = resp.json()
            adapter.debug('Subrace via API', extra={'subrace': subrace_slug})
        except Exception:
            adapter.warning('Subrace não encontrada na API, carregando localmente', extra={'subrace': subrace_slug})
            subrace_data = subraces.get(subrace_slug, {})
            adapter.debug('Subrace local', extra={'subrace_data': subrace_data})

    bonus_total = {}
    for b in race_data.get('ability_bonuses', []):
        idx = b['ability_score']['index'][:3].lower()
        bonus_total[idx] = bonus_total.get(idx, 0) + b['bonus']
    for b in subrace_data.get('ability_bonuses', []):
        idx = b['ability_score']['index'][:3].lower()
        bonus_total[idx] = bonus_total.get(idx, 0) + b['bonus']
    adapter.debug('Bônus totais a serem aplicados', extra=bonus_total)

    for attr in ATTR_KEYS:
        abbr = attr[:3]
        if abbr in bonus_total:
            original = atributos[attr]
            atributos[attr] += bonus_total[abbr]
            adapter.debug(f'Bônus racial aplicado em {attr}', extra={'original': original, 'bonus': bonus_total[abbr], 'final': atributos[attr]})
    modificadores = {abbr: MOD_TABLE.get(atributos[key], 0) for abbr, key in zip(ABBRS, ATTR_KEYS)}
    adapter.debug('Modificadores após bônus raciais', extra=modificadores)

    salvamentos = [
        {'abbr': s['index'].upper(), 'mod': f"{modificadores.get(s['index'],0):+d}"}
        for s in class_data.get('saving_throws', [])
    ]
    adapter.debug('Saving throws', extra={'saves': salvamentos})
    saving_throw_proficiencies = [s['index'].lower() for s in class_data.get('saving_throws', [])]

    skills_list = [
        {'name': sk, 'mod': f"{modificadores.get(ab.lower(),0):+d}"}
        for sk, ab in SKILLS_MAP.items()
    ]
    adapter.debug('Skills list', extra={'skills': skills_list})

    form_skills = [
        skill['name']
        for skill in skills_list
        if data.get(f"{skill['name']}-prof")
    ]

    skill_block = next(
        (c for c in class_data.get('proficiency_choices', [])
         if any('Skill: ' in opt['item']['name'] for opt in c.get('from', {}).get('options', []))),
        None
    )

    if skill_block:
        how_many = skill_block['choose']
        skill_choices = [
            opt['item']['name'].replace('Skill: ', '')
            for opt in skill_block['from']['options']
            if 'Skill: ' in opt['item']['name']
        ]
    else:
        how_many = 0
        skill_choices = []
    adapter.debug('Extração de perícias disponíveis', extra={'quantidade': how_many, 'opções': skill_choices})

    available_for_class = [
    sk for sk in skill_choices
    if sk not in background_skills
    and sk not in form_skills
    ]

    if how_many <= len(available_for_class):
        class_skill_proficiencies = random.sample(available_for_class, k=how_many)
    else:
        class_skill_proficiencies = available_for_class.copy()

    skill_proficiencies = list(set(
        background_skills
        + form_skills
        + class_skill_proficiencies
    ))

    hit_die = class_data.get('hit_die', 6)
    lvl = int(classlevel) if classlevel.isdigit() else 1
    hp = hit_die + modificadores.get('con',0)
    for _ in range(1, lvl):
        hp += random.randint(1, hit_die) + modificadores.get('con',0)
    adapter.debug('HP calculado', extra={'hit_die': hit_die, 'level': lvl, 'hp': hp})
    total_hd = f'{lvl}d{hit_die}'

    classe_full = f"{classe} ({subclasse}) {classlevel}".strip()
    race_full = race_data.get('name', race) + (f" ({subraca})" if subraca else '')
    xp = XP_BY_LEVEL.get(lvl,0)
    proficiencia = proficiency_by_level[lvl-1]

    background_equipment_list = background_data.get("equipment", [])

    class_equipment_list = [
        f"{e['quantity']}× {e['equipment']['name']}"
        for e in class_data.get('starting_equipment', [])
    ]

    random_choices = pick_starting_equipment_options(
        class_data.get('starting_equipment_options', [])
    )

    all_equipment_list = background_equipment_list + class_equipment_list + random_choices

    formatted_all_equipment = "\n".join(f"- {item}" for item in all_equipment_list)

    #armas
    armas_mods = {}
    armas_dano = {}
    nomes_armas = []

    for item in all_equipment_list:
        nome_limpo = item.split('×')[-1].strip()
        resp_arm = requests.get(f"{api_base}/equipment/{normalize_slug(nome_limpo)}")
        if resp_arm.status_code != 200:
            continue
        arma = resp_arm.json()

        if arma.get('equipment_category', {}).get('index') != 'weapon':
            continue

        props     = [p['index'] for p in arma.get('properties', [])]
        cat_range = arma.get('weapon_range','')
        if 'finesse' in props:
            atributo_usado = 'dex' if modificadores['dex'] >= modificadores['str'] else 'str'
        elif cat_range == 'ranged':
            atributo_usado = 'dex'
        else:
            atributo_usado = 'str'

        base_mod = modificadores[atributo_usado]

        profs_classe = [p['name'].lower() for p in class_data.get('proficiencies',[])]
        tem_prof = any(
            termo in profs_classe
            for termo in [arma.get('name','').lower(),
                          f"{arma.get('weapon_category','')} weapons".lower(),
                          f"{cat_range} weapons".lower(),
                          "simple weapons","martial weapons"]
        )
        prof_bonus = proficiencia if tem_prof else 0
        mod_final  = base_mod + prof_bonus

        dano = ""
        dmg_info = arma.get('damage')
        if dmg_info and 'damage_dice' in dmg_info:
            dano = dmg_info['damage_dice']

        nomes_armas.append(nome_limpo)
        armas_mods[nome_limpo] = mod_final
        armas_dano[nome_limpo] = dano

    ca_base = 10 + modificadores.get('dex', 0)  
    best_armor_ca = None
    tem_armadura = False

    for item in all_equipment_list:
        nome_item = item.split('×')[-1].strip()
        armor_resp = requests.get(f"{api_base}/equipment/{normalize_slug(nome_item)}")
        if armor_resp.status_code != 200:
            continue
        armor_data = armor_resp.json()
        
        if armor_data.get("equipment_category", {}).get("index") != "armor":
            continue

        tem_armadura = True
        armor_class = armor_data.get("armor_class", {})
        base = armor_class.get("base", 10)
        dex_bonus = armor_class.get("dex_bonus", False)
        max_bonus = armor_class.get("max_bonus", None)

        mod_dex = modificadores.get('dex', 0)
        if not dex_bonus:
            total_ca = base
        elif max_bonus is not None:
            total_ca = base + min(mod_dex, max_bonus)
        else:
            total_ca = base + mod_dex

        if best_armor_ca is None or total_ca > best_armor_ca:
            best_armor_ca = total_ca

    if tem_armadura:
        ca_final = best_armor_ca
    elif classe.lower() == "barbarian":
        ca_final = 10 + modificadores.get('dex', 0) + modificadores.get('con', 0)
    elif classe.lower() == "monk":
        ca_final = 10 + modificadores.get('dex', 0) + modificadores.get('wis', 0)
    else:
        ca_final = 10 + modificadores.get('dex', 0)

    #outras proficiencias
    outras_proficiencias_background = [
        prof.get('name') for prof in background_data.get('tool_proficiencies', [])
    ]

    #idiomas
    race_languages = [lang['name'] for lang in race_data.get('languages', [])]

    lang_opts = background_data.get('language_options') or {}
    choose_val = lang_opts.get('choose', 0)

    if not isinstance(choose_val, int):
        how_many_backgrounds_languages = 0
    else:
        how_many_backgrounds_languages = choose_val

    if 0 < how_many_backgrounds_languages <= len(LANGUAGES):
        choice_background_languages = random.sample(LANGUAGES, k=how_many_backgrounds_languages)
    else:
        choice_background_languages = []


    idiomas = race_languages + choice_background_languages + outras_proficiencias_background

    idiomas = "\n".join(f"- {idioma}" for idioma in idiomas)

    #traços de personalidade
    personality_traits = background_data.get('personality_traits', {}).get('options')
    personality_traits = random.choice(personality_traits) if personality_traits else None
    ideals = background_data.get('ideals', {}).get('options')
    ideals = random.choice(ideals) if ideals else None
    bonds = background_data.get('bonds', {}).get('options')
    bonds = random.choice(bonds) if bonds else None
    flaws = background_data.get('flaws', {}).get('options')
    flaws = random.choice(flaws) if flaws else None

    context = {
        'lang': lang, 'translations': translations,
        'charname': nome, 'classe': classe_full, 'background': background_slug,
        'playername': playername, 'race': race_full, 'subrace': subrace_slug,
        'alinhamento': alinhamento, 'experience': experience,
        'atributo': atributos, 'mod': modificadores, 'saves': salvamentos,
        'saving_throw_proficiencies': saving_throw_proficiencies,
        'skill_choices': skill_choices, 'random_skill_proficiencies': skill_proficiencies,
        'hit_die': hit_die,'total_hd': total_hd, 'hp': hp,  'xp': xp,
        'proficiencia': proficiencia, 'speed': speed, 'formatted_all_equipment': formatted_all_equipment,
        'armas': nomes_armas, 'armas_mod': armas_mods, 'ca': ca_final, 'idiomas': idiomas, 'personality_traits': personality_traits,
        'ideals': ideals, 'bonds': bonds, 'flaws': flaws,
    }

    for i, nome in enumerate(nomes_armas[:3]):
        mod = armas_mods[nome]
        dmg = armas_dano.get(nome, "")
        context[f"atkname{i+1}"]   = nome
        context[f"atkbonus{i+1}"]  = f"{'+' if mod>=0 else ''}{mod}"
        context[f"atkdamage{i+1}"] = dmg
    adapter.info('Ficha gerada com sucesso', extra={'charname': nome})
    request.session['ultima_ficha'] = context

    logger.debug("Background data:\n%s", pprint.pformat(background_data))

    print(f'TESTING OBJECT: {bonds}')


    return render(request, 'pages/criando.html', context)

def ficha(request):
    return render(request, 'pages/login.html')
def login(request):
    return render(request, 'pages/login.html')