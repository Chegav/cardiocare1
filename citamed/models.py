from django.db import models
from django.db.models.fields import IntegerField
from horariomed.models import Horariomed
from paciente.models import Paciente

# Create your models here.
class Citamedica (models.Model):
        codigocitamed = models.AutoField(primary_key=True, null=False)
        codigodehorario = models.ForeignKey (Horariomed, null=False, on_delete=models.CASCADE)
        cedulapac = models.ForeignKey (Paciente, on_delete=models.CASCADE)