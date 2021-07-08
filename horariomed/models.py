from django.db import models
from medico.models import Medico

# Create your models here.
class Horariomed(models.Model):
    codigodehorario= models.AutoField(primary_key=True, null=False)
    cedulamed= models.ForeignKey(Medico, on_delete=models.CASCADE,null=False)
    fecha= models.CharField(max_length=10, null=False)
    hora=models.TimeField(null=False)
