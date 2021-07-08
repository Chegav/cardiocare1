from django.db import models
from superusuario.models import Superusuario
# Create your models here.
class Medico(models.Model):
    cedula= models.CharField(primary_key=True,max_length=10, null=False)
    nombre= models.CharField(max_length=50, null=False)
    apellido= models.CharField(max_length=50, null=False)
    edad=models.IntegerField(null=False)
    direccion= models.CharField(max_length=100, null=False)
    telefono= models.CharField(max_length=10, null=False)
    fechadenacimiento=models.CharField(max_length=10, null=False)
    tiposangre=models.CharField(max_length=4, null=False)
    contrasena=models.CharField(max_length=40, null=False)
    fechadeingreso=models.CharField(max_length=10, null=False)  
    fechadesalida=models.CharField(max_length=10, null=True)  
    licencia=models.CharField(max_length=70, null=False)
    sexo=models.CharField(max_length=1, null=False)
    estado=models.BooleanField(null=False)
    ced_creador=models.ForeignKey(Superusuario, on_delete=models.CASCADE, null=False)
