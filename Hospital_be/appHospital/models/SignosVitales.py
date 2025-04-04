from django.db import models
from .Paciente import ClasePaciente
from datetime import datetime

class ClaseSignosVitales(models.Model):
    id_vitales = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(ClasePaciente, related_name='SignosVitales', on_delete=models.CASCADE)
    oximetria = models.FloatField(default=0)
    fRespiratoria = models.FloatField(default=0)
    fCardiaca = models.FloatField(default=0)
    temperatura = models.FloatField(default=0)
    pArterial = models.FloatField(default=0)
    glicemias = models.FloatField(default=0)
    fechaHora=models.DateTimeField(default=datetime.now, blank=True)