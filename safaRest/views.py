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

def crear_restaurante (request):
    if request.method=="GET":
        return render(request, 'crear_restaurante.html', {'tipos_restaurante':TipoRestaurante.values})
    else:
        nuevo_restaurante=Restaurante()
        nuevo_restaurante.nombre=request.POST.get("nombre")
        nuevo_restaurante.ciudad = request.POST.get("ciudad")
        nuevo_restaurante.capacidad = int(request.POST.get("capacidad")) #Recibe el número como string, pero en la BD es un entero
        nuevo_restaurante.fecha_fundacion = request.POST.get("fecha") #Usar el mismo nombre en POST.get() que el id del formulario en el html
        nuevo_restaurante.tipo =TipoRestaurante.values[TipoRestaurante.value.index(request.POST.get("tipo_restaurante"))]
        Restaurante.save(nuevo_restaurante)
        return render(request, "inicio.html")
