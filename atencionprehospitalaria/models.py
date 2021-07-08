from django.db import models
from paramedico.models import Paramedico
from emergencia.models import Emergencia

# Create your models here.
class Atencionprehospitalaria(models.Model):
    idatencion = models.AutoField(primary_key=True,null=False)
    codigoemergencia = models.ForeignKey(Emergencia, null = False, on_delete=models.CASCADE)
    ced_paramed = models.ForeignKey(Paramedico, null = False, on_delete=models.CASCADE)
    presion = models.IntegerField(null=False)
    saturacion = models.IntegerField(null=False)
    descripcion = models.CharField(max_length=500,null=False)
    fecharegisto = models.CharField(max_length=10, null=False)
