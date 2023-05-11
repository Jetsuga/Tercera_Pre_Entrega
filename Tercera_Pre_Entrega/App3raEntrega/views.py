from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

def inicio(request):
    return render(request, "inicio.html")

def Mostrar_Juego(request):
    lista = Juego.objects.all()
    return render(request, "Juegos.html", {"Juegos": lista})

def Mostrar_Mando(request):
    lista = Mando.objects.all()
    return render(request, "Mando.html", {"Mando": lista})

def Mostrar_PapasFritas(request):
    lista = PapasFritas.objects.all()
    return render(request, "PapasFritas.html", {"PapasFritas": lista})

def Juego_formulario(request):
    if request.method == 'POST':
        mi_formulario = Juego_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            juego = Juego(titulo=request.POST['titulo'], creador=request.POST['creador'], genero=request.POST['genero'], Descripcion=request.POST['Descripcion'])
            juego.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Juego_Formulario()
        return render(request, "Juegos_formulario.html", {"mi_formulario": mi_formulario})
    
def Mando_formulario(request):
    if request.method == 'POST':
        mi_formulario = Mando_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            mando = Mando(Marca=request.POST['Marca'], modelo=request.POST['modelo'], genero=request.POST['genero'], descripcion=request.POST['descripcion'])
            mando.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = Mando_Formulario()
        return render(request, "Mando_formulario.html", {"mi_formulario": mi_formulario})
    
def PapasFritas_formulario(request):
    if request.method == 'POST':
        mi_formulario = PapasFritas_Formulario(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            papasFritas = PapasFritas(Paquete=request.POST['Paquete'], marca=request.POST['marca'], Sabor=request.POST['Sabor'])
            papasFritas.save()
        return render(request, "inicio.html")
    else:
        mi_formulario = PapasFritas_Formulario()
        return render(request, "PapasFritas_formulario.html", {"mi_formulario": mi_formulario})

def busqueda_genero(request):
    return render(request, "busqueda_genero.html")

def buscar(request):
    if request.GET["genero"]:
        genero = request.GET["genero"]
        Mostrar_Juego = Juego.objects.filter(genero=genero)
        return render(request, "resultados_busqueda.html", {"Juegos por genero": Juego, "genero": genero})
    else:
        return HttpResponse("No enviaste info, por favor ingresa algo nuevamente")