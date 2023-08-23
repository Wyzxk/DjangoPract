from django.http import HttpResponse
import datetime
from django.shortcuts import render

def saludar(request):
    
    return HttpResponse("Hola Mundo")


def fecha(request):
    fecha = datetime.datetime.now()
    return HttpResponse("<h1>La fecha actual es: %s </h1>" %fecha)

def edades(request,edad,año):
 añoAct = 2023
 edadAct = edad
 edadFut = (año - añoAct) + edad
 documento = "<h2>Su edad actual es {} y su edad en el año {} será {}</h2>".format(edad,año,edadFut)
 return HttpResponse(documento)

def plantilla(request):
    nombre = 'Jhon'    
    # (también podemos pasarle un metodo de una clase)
    fecha = datetime.datetime.now()
    # (tema 9)
    listica = ['Mazda','Toyota','Nissan','Ferrari']
    return render(request, 'index.html',{
    #    (Aquí va el diccionario, recordemos que el diccionario tiene "clave":, valor)
       "nombre" : nombre,
       "fecha" : fecha,
       "listica" : listica,
 })
