backgrounds = {
    "guild-artisan": { 
        "index": "guild-artisan",
        "name": "Guild Artisan",
        "url": "/api/2014/backgrounds/guild-artisan",
        "desc": [
            "You are a member of an artisan’s guild, skilled in your craft and recognized by your fellows."
        ],
        "skill_proficiencies": [
            {"index": "skill-insight", "name": "Insight", "url": "/api/2014/proficiencies/skill-insight"},
            {"index": "skill-persuasion", "name": "Persuasion", "url": "/api/2014/proficiencies/skill-persuasion"}
        ],
        "tool_proficiencies": [
            {"index": "artisan-tools", "name": "One type of artisan’s tools", "url": "/api/2014/proficiencies/artisan-tools"}
        ],
        "equipment": [
            "A set of artisan’s tools (one of your choice)",
            "A letter of introduction from your guild",
            "A set of traveler's clothes",
            "15 gp"
        ],
        "feature": {
            "name": "Guild Membership",
            "desc": [
                "As a member of your guild you can call upon the aid of fellow members, "
                "and you have access to guild halls and safe lodging in cities where your guild has a presence."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I believe that anything worth doing is worth doing right. I can’t help it—I'm a perfectionist.",
                "I’m always calm, no matter what the situation. I never raise my voice or let my emotions control me."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Community. It is the duty of all civilized people to strengthen the bonds of community and the security of civilization. (Good)",
                "Greed. The guild is an instrument to acquire wealth. (Evil)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "The workshop where I learned my trade is the most important place in the world to me.",
                "I will do anything to protect the members of my guild."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I’m quick to assume that someone is trying to cheat me.",
                "No one must ever learn that I once stole money from guild coffers."
            ]
        }
    },
    "entertainer": { #artista
        "index": "entertainer",
        "name": "Entertainer",
        "url": "/api/2014/backgrounds/entertainer",
        "desc": [
            "You flourish in front of an audience. You know how to entrance them, entertain them, and even inspire them."
        ],
        "skill_proficiencies": [
            {"index": "skill-acrobatics", "name": "Acrobatics", "url": "/api/2014/proficiencies/skill-acrobatics"},
            {"index": "skill-performance", "name": "Performance", "url": "/api/2014/proficiencies/skill-performance"}
        ],
        "tool_proficiencies": [
            {"index": "disguise-kit", "name": "Disguise Kit", "url": "/api/2014/proficiencies/disguise-kit"},
            {"index": "musical-instrument", "name": "One type of musical instrument", "url": "/api/2014/proficiencies/musical-instrument"}
        ],
        "equipment": [
            "A musical instrument (one of your choice)",
            "The favor of an admirer",
            "A costume",
            "15 gp"
        ],
        "feature": {
            "name": "By Popular Demand",
            "desc": [
                "You can always find a place to perform, usually in an inn or tavern but possibly with a circus, at a theater, or even in a noble’s court."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I know a story relevant to almost every situation.",
                "Whenever I come to a new place, I collect local rumors and spread gossip."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Beauty. When I perform, I make the world better than it was. (Good)",
                "Self‑expression. The world is in need of new ideas and bold action. (Chaotic)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "My instrument is my most treasured possession, and it reminds me of someone I love.",
                "I will do anything to prove myself superior to my rival."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I’ll do anything to win fame and renown.",
                "I’m a sucker for a pretty face."
            ]
        }
    },
    "charlatan": { #charlatão
        "index": "charlatan",
        "name": "Charlatan",
        "url": "/api/2014/backgrounds/charlatan",
        "desc": [
            "You have always had a way with people. You know what makes them tick, and you know how to manipulate them."
        ],
        "skill_proficiencies": [
            {"index": "skill-deception", "name": "Deception", "url": "/api/2014/proficiencies/skill-deception"},
            {"index": "skill-insight", "name": "Insight", "url": "/api/2014/proficiencies/skill-insight"}
        ],
        "tool_proficiencies": [
            {"index": "disguise-kit", "name": "Disguise Kit", "url": "/api/2014/proficiencies/disguise-kit"},
            {"index": "forgery-kit", "name": "Forgery Kit", "url": "/api/2014/proficiencies/forgery-kit"}
        ],
        "equipment": [
            "A set of weighted dice",
            "A deck of marked cards",
            "A fine set of clothes",
            "15 gp"
        ],
        "feature": {
            "name": "False Identity",
            "desc": [
                "You have created a second identity that includes documentation, established acquaintances, and disguises that allow you to assume that persona."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I fall in and out of love easily, and am always pursuing someone.",
                "I have a joke for every occasion, especially occasions where humor is inappropriate."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Independence. I am a free spirit—no one tells me what to do. (Chaotic)",
                "Honesty. There’s a benefit to being frank. (Lawful)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I owe everything to my mentor—a horrible person who’s probably rotting in jail.",
                "Someone I loved died because of I mistake I made. That will never happen again."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I can’t resist a pretty face.",
                "I’m always in debt. I spend my ill-gotten gains on decadent luxuries faster than I bring them in."
            ]
        }
    },
    "criminal": {#criminoso
        "index": "criminal",
        "name": "Criminal",
        "url": "/api/2014/backgrounds/criminal",
        "desc": [
            "You are an experienced criminal with a history of breaking the law. You have underworld connections and know how to get things."
        ],
        "skill_proficiencies": [
            {"index": "skill-deception", "name": "Deception", "url": "/api/2014/proficiencies/skill-deception"},
            {"index": "skill-stealth", "name": "Stealth", "url": "/api/2014/proficiencies/skill-stealth"}
        ],
        "tool_proficiencies": [
            {"index": "thieves-tools", "name": "Thieves’ Tools", "url": "/api/2014/proficiencies/thieves-tools"}
        ],
        "equipment": [
            "A crowbar",
            "A set of dark common clothes including a hood",
            "15 gp"
        ],
        "feature": {
            "name": "Criminal Contact",
            "desc": [
                "You have a reliable and trustworthy contact in the criminal underworld."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "The first thing I do in a new place is note the locations of everything valuable—or where such things could be hidden.",
                "I’m always calm, no matter what the situation."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Honor among thieves. (Neutral)",
                "Freedom. Chains are meant to be broken, as are those who would forge them. (Chaotic)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I will become the greatest thief that ever lived.",
                "I’m guilty of a terrible crime and I’m trying to atone for it."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "When I see something valuable, I can’t think about anything but how to steal it.",
                "An innocent person is in prison for a crime I committed. I’m okay with that."
            ]
        }
    },
    "hermit": {
        "index": "hermit",
        "name": "Hermit",
        "url": "/api/2014/backgrounds/hermit",
        "desc": [
            "You lived in seclusion—either in a sheltered community such as a monastery, or entirely alone—for a formative part of your life."
        ],
        "skill_proficiencies": [
            {"index": "skill-medicine", "name": "Medicine", "url": "/api/2014/proficiencies/skill-medicine"},
            {"index": "skill-religion", "name": "Religion", "url": "/api/2014/proficiencies/skill-religion"}
        ],
        "tool_proficiencies": [
            {"index": "herbalism-kit", "name": "Herbalism Kit", "url": "/api/2014/proficiencies/herbalism-kit"}
        ],
        "equipment": [
            "A scroll case stuffed full of notes from your studies",
            "A winter blanket",
            "A set of common clothes",
            "5 gp"
        ],
        "feature": {
            "name": "Discovery",
            "desc": [
                "The quiet seclusion of your extended hermitage gave you access to a unique and powerful discovery."
            ]
        },
        "language_options": {
            "choose": 1,
            "from": ["language"]
        },
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I’ve been isolated for so long that I rarely speak, preferring gestures and the occasional grunt.",
                "I’m oblivious to etiquette and social expectations."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Self-Knowledge. If you know yourself, there’s nothing left to know. (Any)",
                "Greater Good. My gifts are meant to be shared with all, not used for my own benefit. (Good)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I entered seclusion to hide from the ones who might still be hunting me.",
                "I’m still seeking the enlightenment I pursued in my seclusion."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I harbor dark, bloodthirsty thoughts that my isolation failed to quell.",
                "I let my need to win arguments overshadow friendships and harmony."
            ]
        }
    },
    "outlander": {
        "index": "outlander",
        "name": "Outlander",
        "url": "/api/2014/backgrounds/outlander",
        "desc": [
            "You grew up in the wilds, far from civilization and the comforts of town and technology."
        ],
        "skill_proficiencies": [
            {"index": "skill-athletics", "name": "Athletics", "url": "/api/2014/proficiencies/skill-athletics"},
            {"index": "skill-survival", "name": "Survival", "url": "/api/2014/proficiencies/skill-survival"}
        ],
        "tool_proficiencies": [
            {"index": "musical-instrument", "name": "One type of musical instrument", "url": "/api/2014/proficiencies/musical-instrument"}
        ],
        "equipment": [
            "A staff",
            "A hunting trap",
            "A trophy from an animal you killed",
            "A set of traveler’s clothes",
            "10 gp"
        ],
        "feature": {
            "name": "Wanderer",
            "desc": [
                "You have an excellent memory for maps and geography, and you can always recall the general layout of terrain."
            ]
        },
        "language_options": {
            "choose": 1,
            "from": ["language"]
        },
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I watch over my friends as if they were a litter of newborn pups.",
                "I once ran twenty-five miles without stopping to warn my clan of an approaching orc horde."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Change. Life is like the seasons, in constant change. (Chaotic)",
                "Glory. I must earn glory in battle. (Any)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "My family, clan, or tribe is the most important thing in my life.",
                "I will bring terrible wrath down on the evildoers who destroyed my homeland."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I am slow to trust members of other races, tribes, and societies.",
                "There’s no room for caution in a life lived to the fullest."
            ]
        }
    },
        "folk-hero": {
            "index": "folk-hero",
            "name": "Folk Hero",
            "url": "/api/2014/backgrounds/folk-hero",
            "desc": [
                "You come from a humble social rank, but you are destined for so much more."
            ],
            "skill_proficiencies": [
                {"index": "skill-animal-handling", "name": "Animal Handling", "url": "/api/2014/proficiencies/skill-animal-handling"},
                {"index": "skill-survival", "name": "Survival", "url": "/api/2014/proficiencies/skill-survival"}
            ],
            "tool_proficiencies": [
                {"index": "artisan-tools", "name": "One type of artisan's tools", "url": "/api/2014/proficiencies/artisan-tools"},
                {"index": "vehicles-land", "name": "Vehicles (land)", "url": "/api/2014/proficiencies/vehicles-land"}
            ],
            "equipment": [
                "A set of artisan’s tools",
                "A shovel",
                "An iron pot",
                "A set of common clothes",
                "10 gp"
            ],
            "feature": {
                "name": "Rustic Hospitality",
                "desc": [
                    "You come from the ranks of the common folk, and you fit in among them with ease."
                ]
            },
            "language_options": None,
            "personality_traits": {
                "option_set_type": "options_array",
                "options": [
                    "I judge people by their actions, not their words.",
                    "If someone is in trouble, I’m always ready to lend help."
                ]
            },
            "ideals": {
                "option_set_type": "options_array",
                "options": [
                    "Respect. People deserve to be treated with dignity. (Good)",
                    "Freedom. Tyrants must not be allowed to oppress the people. (Chaotic)"
                ]
            },
            "bonds": {
                "option_set_type": "options_array",
                "options": [
                    "I have a family to protect. I must make them proud.",
                    "I protect those who cannot protect themselves."
                ]
            },
            "flaws": {
                "option_set_type": "options_array",
                "options": [
                    "I have trouble trusting my allies.",
                    "I’m convinced of the significance of my destiny, and blind to my shortcomings."
                ]
            }
        },
        "sailor": {
            "index": "sailor",
            "name": "Sailor",
            "url": "/api/2014/backgrounds/sailor",
            "desc": [
                "You sailed on a seagoing vessel for years. In that time, you faced down mighty storms, monsters of the deep, and those who wanted to sink your craft."
            ],
            "skill_proficiencies": [
                {"index": "skill-athletics", "name": "Athletics", "url": "/api/2014/proficiencies/skill-athletics"},
                {"index": "skill-perception", "name": "Perception", "url": "/api/2014/proficiencies/skill-perception"}
            ],
            "tool_proficiencies": [
                {"index": "navigator-tools", "name": "Navigator’s tools", "url": "/api/2014/proficiencies/navigator-tools"},
                {"index": "vehicles-water", "name": "Vehicles (water)", "url": "/api/2014/proficiencies/vehicles-water"}
            ],
            "equipment": [
                "A belaying pin (club)",
                "50 feet of silk rope",
                "A lucky charm",
                "A set of common clothes",
                "10 gp"
            ],
            "feature": {
                "name": "Ship's Passage",
                "desc": [
                    "You can secure free passage on a sailing ship for yourself and your adventuring companions."
                ]
            },
            "language_options": None,
            "personality_traits": {
                "option_set_type": "options_array",
                "options": [
                    "My friends know they can rely on me, no matter what.",
                    "I enjoy sailing into new ports and making new friends over a flagon of ale."
                ]
            },
            "ideals": {
                "option_set_type": "options_array",
                "options": [
                    "Respect. The thing that keeps a ship together is mutual respect. (Good)",
                    "Fairness. We all do the work, so we all share in the rewards. (Lawful)"
                ]
            },
            "bonds": {
                "option_set_type": "options_array",
                "options": [
                    "I'm loyal to my captain first, everything else second.",
                    "The ship is the most important thing—more important even than the gods."
                ]
            },
            "flaws": {
                "option_set_type": "options_array",
                "options": [
                    "I follow orders, even if I think they’re wrong.",
                    "Once someone questions my courage, I never back down no matter how dangerous the situation."
                ]
            }
        },
        "noble": {
        "index": "noble",
        "name": "Noble",
        "url": "/api/2014/backgrounds/noble",
        "desc": [
            "You understand wealth, power, and privilege. You carry a noble title, and your family owns land."
        ],
        "skill_proficiencies": [
            {"index": "skill-history", "name": "History", "url": "/api/2014/proficiencies/skill-history"},
            {"index": "skill-persuasion", "name": "Persuasion", "url": "/api/2014/proficiencies/skill-persuasion"}
        ],
        "tool_proficiencies": [
            {"index": "gaming-set", "name": "One type of gaming set", "url": "/api/2014/proficiencies/gaming-set"}
        ],
        "equipment": [
            "A set of fine clothes",
            "A signet ring",
            "A scroll of pedigree",
            "A purse containing 25 gp"
        ],
        "feature": {
            "name": "Position of Privilege",
            "desc": [
                "Thanks to your noble birth, people are inclined to think the best of you."
            ]
        },
        "language_options": {
            "choose": 1,
            "from": ["language"]
        },
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "My eloquent flattery makes everyone I talk to feel like the most wonderful person in the world.",
                "The common folk love me for my kindness and generosity."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Responsibility. It is my duty to respect the authority of those above me. (Lawful)",
                "Noblesse Oblige. I must prove that I can handle myself without the coddling of my family. (Good)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I will face any challenge to win the approval of my family.",
                "My house’s alliance with another noble family must be sustained at all costs."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I hide a truly scandalous secret that could ruin my family forever.",
                "I too often hear veiled insults and threats in every word addressed to me, and I’m quick to anger."
            ]
        }
    },
    "urchin": {
        "index": "urchin",
        "name": "Urchin",
        "url": "/api/2014/backgrounds/urchin",
        "desc": [
            "You grew up on the streets alone, orphaned, and poor, learning to fend for yourself."
        ],
        "skill_proficiencies": [
            {"index": "skill-sleight-of-hand", "name": "Sleight of Hand", "url": "/api/2014/proficiencies/skill-sleight-of-hand"},
            {"index": "skill-stealth", "name": "Stealth", "url": "/api/2014/proficiencies/skill-stealth"}
        ],
        "tool_proficiencies": [
            {"index": "disguise-kit", "name": "Disguise Kit", "url": "/api/2014/proficiencies/disguise-kit"},
            {"index": "thieves-tools", "name": "Thieves' Tools", "url": "/api/2014/proficiencies/thieves-tools"}
        ],
        "equipment": [
            "A small knife",
            "A map of the city you grew up in",
            "A pet mouse",
            "A token to remember your parents by",
            "A set of common clothes",
            "10 gp"
        ],
        "feature": {
            "name": "City Secrets",
            "desc": [
                "You know the secret patterns and flow to cities and can find passages through the urban sprawl others would miss."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I hide scraps of food and trinkets away in my pockets.",
                "I ask a lot of questions."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Change. The low are lifted up, and the high and mighty are brought down. (Chaotic)",
                "Redemption. There's a spark of good in everyone. (Good)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I owe my survival to another urchin who taught me to live on the streets.",
                "I will honor the memory of my parents."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "It's not stealing if I need it more than someone else.",
                "I will never fully trust anyone other than myself."
            ]
        }
    },
    "sage": {
        "index": "sage",
        "name": "Sage",
        "url": "/api/2014/backgrounds/sage",
        "desc": [
            "You spent years learning the lore of the multiverse, gathering knowledge in libraries, universities, or from mentors."
        ],
        "skill_proficiencies": [
            {"index": "skill-arcana", "name": "Arcana", "url": "/api/2014/proficiencies/skill-arcana"},
            {"index": "skill-history", "name": "History", "url": "/api/2014/proficiencies/skill-history"}
        ],
        "tool_proficiencies": [],
        "equipment": [
            "A bottle of black ink",
            "A quill",
            "A small knife",
            "A letter from a dead colleague posing a question you have not yet been able to answer",
            "A set of common clothes",
            "10 gp"
        ],
        "feature": {
            "name": "Researcher",
            "desc": [
                "When you attempt to learn or recall a piece of lore, if you don't know that information, you often know where and from whom you can obtain it."
            ]
        },
        "language_options": {
            "choose": 2,
            "from": ["language"]
        },
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I use polysyllabic words to convey the impression of great erudition.",
                "I’ve read every book in the world’s greatest libraries—or I like to boast that I have."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Knowledge. The path to power and self-improvement is through knowledge. (Neutral)",
                "Beauty. What is beautiful points us beyond itself toward what is true. (Good)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I’ve been searching my whole life for the answer to a certain question.",
                "I sold my soul for knowledge. I hope to do great deeds and win it back."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I am easily distracted by the promise of information.",
                "Most people scream and run when they see a demon. I stop and take notes on its anatomy."
            ]
        }
    },
    "soldier": {
        "index": "soldier",
        "name": "Soldier",
        "url": "/api/2014/backgrounds/soldier",
        "desc": [
            "War has been your life for as long as you care to remember. You trained as a youth, studied the use of weapons and armor, and lived through battles."
        ],
        "skill_proficiencies": [
            {"index": "skill-athletics", "name": "Athletics", "url": "/api/2014/proficiencies/skill-athletics"},
            {"index": "skill-intimidation", "name": "Intimidation", "url": "/api/2014/proficiencies/skill-intimidation"}
        ],
        "tool_proficiencies": [
            {"index": "gaming-set", "name": "One type of gaming set", "url": "/api/2014/proficiencies/gaming-set"},
            {"index": "vehicles-land", "name": "Vehicles (land)", "url": "/api/2014/proficiencies/vehicles-land"}
        ],
        "equipment": [
            "An insignia of rank",
            "A trophy taken from a fallen enemy",
            "A set of bone dice or deck of cards",
            "A set of common clothes",
            "10 gp"
        ],
        "feature": {
            "name": "Military Rank",
            "desc": [
                "You have a military rank from your career as a soldier. Soldiers loyal to your former military organization still recognize your authority and influence."
            ]
        },
        "language_options": None,
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I’m always polite and respectful.",
                "I’ve lost too many friends, and I’m slow to make new ones."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Greater Good. Our lot is to lay down our lives in defense of others. (Good)",
                "Nation. My city, nation, or people are all that matter. (Any)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I would still lay down my life for the people I served with.",
                "Someone saved my life on the battlefield. To this day, I will never leave a friend behind."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I made a terrible mistake in battle that cost many lives—and I would do anything to keep that secret.",
                "I obey the law, even if the law causes misery."
            ]
        }
    },
    "acolyte": {
        "index": "acolyte",
        "name": "Acolyte",
        "url": "/api/2014/backgrounds/acolyte",
        "desc": [
            "You have spent your life in the service of a temple to a specific god or pantheon of gods. You act as an intermediary between the realm of the holy and the mortal world, performing sacred rites and offering sacrifices."
        ],
        "skill_proficiencies": [
            {
                "index": "skill-insight",
                "name": "Insight",
                "url": "/api/2014/proficiencies/skill-insight"
            },
            {
                "index": "skill-religion",
                "name": "Religion",
                "url": "/api/2014/proficiencies/skill-religion"
            }
        ],
        "tool_proficiencies": [],
        "equipment": [
            "A holy symbol",
            "A prayer book or prayer wheel",
            "5 sticks of incense",
            "Vestments",
            "A set of common clothes",
            "15 gp"
        ],
        "feature": {
            "name": "Shelter of the Faithful",
            "desc": [
                "As an acolyte, you command the respect of those who share your faith, and you can perform the religious ceremonies of your deity. You and your adventuring companions can expect to receive free healing and care at a temple, shrine, or other established presence of your faith."
            ]
        },
        "language_options": {
            "choose": 2,
            "from": "all"  # Indica que deve puxar de uma lista separada
        },
        "personality_traits": {
            "option_set_type": "options_array",
            "options": [
                "I idolize a particular hero of my faith and constantly refer to that person’s deeds and example.",
                "I can find common ground between the fiercest enemies, empathizing with them and always working toward peace."
            ]
        },
        "ideals": {
            "option_set_type": "options_array",
            "options": [
                "Tradition. The ancient traditions of worship and sacrifice must be preserved and upheld. (Lawful)",
                "Charity. I always try to help those in need, no matter what the personal cost. (Good)"
            ]
        },
        "bonds": {
            "option_set_type": "options_array",
            "options": [
                "I would die to recover an ancient relic of my faith that was lost long ago.",
                "I owe my life to the priest who took me in when my parents died."
            ]
        },
        "flaws": {
            "option_set_type": "options_array",
            "options": [
                "I judge others harshly, and myself even more severely.",
                "I put too much trust in those who wield power within my temple’s hierarchy."
            ]
        }
    }
}

