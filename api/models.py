from django.db import models

# Create your models here.

class trabajador(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.IntegerField()
    cargo = models.CharField(max_length=50)
    salario = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre + ' ' + self.apellido