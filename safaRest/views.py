from django.shortcuts import render

from .models import *
# Create your views here.

def cargar_pagina_inicio(request):
    return render(request, 'inicio.html')


def listar_restaurantes(request):
    list_restaurantes=Restaurante.objects.all()
    return render(request, 'Lista_restaurantes.html', {'restaurantes': list_restaurantes})

# def buscar_restaurante(request):
#     lugar=request.GET.get("busqueda").replace('"', '')
#     list_retaurantes=Restaurante.objects.get(nombre=nombre_restaurante)
#     return render(request, 'Datos_Restaurante.html', {'rest':list_retaurantes}) #Se usa rest en el html para obtener los datos de esra vista

def buscar_restaurante(request):
    lugar=request.GET.get("busqueda") #lugar tendrá el valor que devuelve el get cuando se le hace un rquest: /safaRest/buscar/?busqueda=Sevilla
    list_restaurantes=Restaurante.objects.filter(ciudad=lugar)
    return render(request, 'Lista_restaurantes.html', {'restaurantes':list_restaurantes}) #Se usa restaurantes en el html para obtener los datos de esra vista


def saludo(request, nombre):
    context={'name': nombre}
    return render(request, 'inicio.html', context)


def decison(request):
    num=3
    context={'num':num}
    return render(request, 'inicio.html', context)

listlenguajes=["python", "java", "php", "C#", "javascript"]

def lista_lenguajes(request):
    context={'listlenguajes': listlenguajes}
    return render(request, "inicio.html", context)
