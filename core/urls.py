from django.urls import path
from .views import home, entrada, register, exit


urlpatterns = [
    path('', home, name='home'),
    path('entrada/', entrada, name='entrada'),
    path('register/', register, name='register'),
    path('logout/', exit, name='exit'),
]