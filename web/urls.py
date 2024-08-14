from django.urls import path, include
from .views import home, about_vista, welcome_vista, contacto, success, logoutyo

urlpatterns = [
    path('', home, name='home'),
    path('acerca/', about_vista, name='acerca'),
    path('bienvenido/', welcome_vista, name='bienvenido'),
    path('contacto/', contacto, name='contacto'),
    path('exito/', success, name='success'),
    path("accounts/", include('django.contrib.auth.urls')),
    path("logout-yo/", logoutyo, name="logout-yo"),
   
]