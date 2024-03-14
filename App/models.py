from django.db import models

# Create your models here.
class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField() 
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre
    
class Curso(models.Model):
    nombre = models.CharField(max_length=30)
    comision = models.IntegerField()

    def __str__(self):
        return self.nombre

class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=40)

    def __str__(self):
        return self.nombre

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    fechaEntrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return self.nombre