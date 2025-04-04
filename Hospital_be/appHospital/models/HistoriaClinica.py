from django.db import models
from .Paciente import ClasePaciente

class ClaseHistoriaClinica(models.Model):
    id_HistoriaClinica = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(ClasePaciente, related_name='HistoriaClinica', on_delete=models.CASCADE)
    sugerencias = models.CharField('Sugerencias', max_length = 30)
    diagnostico = models.CharField('Diagnostico', max_length = 30)
    entorno = models.CharField('Entorno', max_length = 30)
    fecha = models.DateTimeField()
    descripcion =  models.CharField('Descripcion', max_length = 30)
