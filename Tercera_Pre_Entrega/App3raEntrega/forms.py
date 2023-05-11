from django import forms

class Juego_Formulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    creador = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    Descripcion = forms.CharField(max_length=200)

class Mando_Formulario(forms.Form):
    Marca = forms.CharField(max_length=200)
    modelo = forms.CharField(max_length=200)
    genero = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)

class PapasFritas_Formulario(forms.Form):
    Paquete = forms.CharField(max_length=200)
    marca = forms.CharField(max_length=200)
    Sabor = forms.CharField(max_length=200)


