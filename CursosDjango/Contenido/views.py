from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.

#Implementacion del menu solocitado


#Pagina principal donde se da la bienvenida
def principal(request):
    return render(request,"Contenido/principal.html")

#Pagina de contenido en esta se muestra el muenu implementado
#con los diferentes cursos solocitados
def curso(request):
   return render(request, "Contenido/curso.html")

#Pagina de contacto, en esta el usuario puede pedir informacion
#acerca de los cursos disponibles

def contactos(request):
    return render(request, "Contenido/contactoOri.html")

def example(request):
    return render(request, "Contenido/example.html")