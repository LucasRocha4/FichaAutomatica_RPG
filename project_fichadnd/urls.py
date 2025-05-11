from django.urls import path
from app_fichadnd.views import home, criando, ficha, login
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', home, name='home'),
    path('criando/', criando, name='criando'),
    path('ficha/', ficha, name='ficha'),
    path('login/', login, name="login")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])