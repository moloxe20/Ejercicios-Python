# Este ejemplo asume que Django está instalado y configurado

# models.py
from django.db import models  # type: ignore # Importamos el módulo models de Django

# Definimos un modelo para almacenar información de personas
class Persona(models.Model):
    nombre = models.CharField(max_length=100)  # Definimos un campo de texto con un tamaño máximo de 100 caracteres
    edad = models.IntegerField()  # Definimos un campo entero para la edad

# views.py
from django.shortcuts import render  # type: ignore # Importamos el módulo render para renderizar plantillas
from .models import Persona  # Importamos el modelo Persona

# Definimos una vista para mostrar una lista de personas
def lista_personas(request):
    personas = Persona.objects.all()  # Obtenemos todas las personas de la base de datos
    return render(request, 'lista_personas.html', {'personas': personas})  # Renderizamos la plantilla con la lista de personas

# urls.py
from django.urls import path  # type: ignore # Importamos el módulo path para definir rutas
from . import views  # Importamos el módulo views

urlpatterns = [
    path('personas/', views.lista_personas, name='lista_personas'),  # Definimos una ruta para la vista lista_personas
]
