from django.db import models

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=64, help_text='Ingresa el nombre del director')
    apellido = models.CharField(max_length=64, help_text='Ingresa el apellido del director')
    
    def __str__(self) -> str:
        return self.name
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=64)
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null=True)
    descripcion =  models.TextField(max_length=255, help_text='Ingresa descripcion de la pelicula')
    

    def __str__(self) -> str:
        return self.titulo 
