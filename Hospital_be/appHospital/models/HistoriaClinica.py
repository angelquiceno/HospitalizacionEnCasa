from django.db import models
from .Paciente import ClasePaciente


class ClaseHistoriaClinica(models.Model):
    id_HistoriaClinica = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(
        ClasePaciente, related_name="HistoriaClinica", on_delete=models.CASCADE
    )
    sugerencias = models.TextField("Sugerencias", blank=True)
    diagnostico = models.TextField("Diagnostico")
    entorno = models.TextField("Entorno", blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField("Descripcion")

    def __str__(self):
        return (
            f"Historia Clínica - {self.id_paciente} - {self.fecha.strftime('%Y-%m-%d')}"
        )

    class Meta:
        verbose_name = "Historia Clínica"
        verbose_name_plural = "Historias Clínicas"
        ordering = ["-fecha"]
