from django.contrib import admin
from django.urls import path
from .views import *
from .import views

import safaRest

urlpatterns = [
    path('', cargar_pagina_inicio),
    #path(pseudónimo de la vista y palabra que se pone en el buscador para acceder al html al que pertenece la vista, nombre del método en views)
    path('restaurantes', listar_restaurantes),
    path('<str:nombre>/', views.saludo, name='saludo'),
    path('decision/', views.decison, name='decision'),
    path('lista_lenguajes/', views.lista_lenguajes, name="lista_lenguajes"),
    path('buscar/', buscar_restaurante),



]