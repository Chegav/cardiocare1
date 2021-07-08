from django.db import models
from superusuario.models import Superusuario

# Create your models here.
class Paramedico(models.Model): 
    cedula = models.CharField(primary_key=True, max_length=10, null=False)
    nombre = models.CharField(max_length=50, null=False)
    apellido = models.CharField(max_length=50, null=False)
    edad = models.IntegerField( null=False)
    direccion = models.CharField(max_length=100, null=False)
    telefono = models.CharField(max_length=10, null=False)
    fechanacimiento = models.CharField(max_length=10, null = False)
    tiposangre = models.CharField(max_length=4, null=False)
    fechaingreso = models.CharField(max_length=10, null=False)
    fechasalida = models.CharField( max_length=10, null=True)
    titulo = models.CharField(max_length=50, null=False)
    sexo = models.CharField(max_length=1, null=False)
    estado = models.BooleanField(default=True, null=False)
    contrasena = models.CharField(max_length=40, null=False)
    ced_creador = models.ForeignKey(Superusuario, on_delete=models.CASCADE, null=False, default='0000000000')
