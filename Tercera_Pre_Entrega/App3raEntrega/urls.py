from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('Juegos', Mostrar_Juego, name='Juegos'),
    path('Mandos', Mostrar_Mando, name='Mandos'),
    path('Papas-Fritas', Mostrar_PapasFritas, name='PapasFritas'),
    path('agregarJuegos', Juego_formulario, name='agregarJuegos'),
    path('agregarMando', Mando_formulario, name='agregarMando'),
    path('agregarPapas', PapasFritas_formulario, name='agregarPapas'),
    path('', inicio, name='Inicio'),
    path('busq-gen', busqueda_genero, name="BusquedaGenero"),
    path('buscar', buscar, name="Buscar"),
]