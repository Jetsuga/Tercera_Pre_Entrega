from django.db import models

# Create your models here.
class Juego(models.Model):
    titulo = models.CharField(max_length=200)
    creador = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    Descripcion = models.TextField()
    def __str__(self):
        return f"{self.titulo} - {self.creador} - {self.genero}"

class Mando(models.Model):
    Marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    genero = models.CharField(max_length=200)
    descripcion = models.TextField()
    def __str__(self):
        return f"{self.Marca} - {self.modelo} - {self.genero}"

class PapasFritas(models.Model):
    Paquete = models.CharField(max_length=200)
    marca = models.CharField(max_length=200)
    Sabor = models.CharField(max_length=200)
    def __str__(self):
        return f"{self.Paquete} - {self.Marca} - {self.Sabor}"
