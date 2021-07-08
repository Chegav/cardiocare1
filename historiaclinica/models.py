from django.db import models
from paciente.models import Paciente
from medico.models import Medico

# Create your models here.
class Historiaclinica (models.Model):
    idhistoria= models.AutoField(primary_key=True, null=False)
    cedpaciente= models.ForeignKey(Paciente, on_delete=models.CASCADE, null=False)
    altura= models.DecimalField(max_digits=5,decimal_places=2, null=False)
    peso= models.DecimalField(max_digits=5,decimal_places=2, null=False)
    saturacion= models.DecimalField(max_digits=5,decimal_places=2, null=False)
    tipodeingreso= models.CharField(max_length=1, null=False)
    fechaderegistro= models.CharField(max_length=10, null=False)
    descripcion = models.CharField(max_length=500, null=False)
    presion= models.IntegerField(null=False)
    cedmedico = models.ForeignKey(Medico, on_delete=models.CASCADE, null=False)