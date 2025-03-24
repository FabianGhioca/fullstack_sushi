from django.urls import path
from . import views

urlpatterns = [
    path('', views.rolls, name='home'),
    path('contattaci', views.contattaci, name='contattaci'),
]