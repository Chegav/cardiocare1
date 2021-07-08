from django.db import models
from django.db.models.fields import IntegerField
from paciente.models import Paciente

# Create your models here.
class Emergencia (models.Model):
    codigoemergencia = models.AutoField(primary_key=True, null=False)
    cedulapaciente = models.ForeignKey(Paciente, on_delete= models.CASCADE, null=False)
    direccion = models.CharField(null=False, max_length=60)

    

    