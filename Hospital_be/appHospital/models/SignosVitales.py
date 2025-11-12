from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .Paciente import ClasePaciente


class ClaseSignosVitales(models.Model):
    id_vitales = models.AutoField(primary_key=True)
    id_paciente = models.ForeignKey(
        ClasePaciente, related_name="SignosVitales", on_delete=models.CASCADE
    )

    # Oximetría: 0-100%
    oximetria = models.FloatField(
        "Oximetría (%)",
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Saturación de oxígeno en sangre (0-100%)",
    )

    # Frecuencia Respiratoria: 5-60 respiraciones por minuto
    fRespiratoria = models.FloatField(
        "Frecuencia Respiratoria",
        validators=[MinValueValidator(5), MaxValueValidator(60)],
        help_text="Respiraciones por minuto (5-60)",
    )

    # Frecuencia Cardíaca: 30-220 latidos por minuto
    fCardiaca = models.FloatField(
        "Frecuencia Cardíaca",
        validators=[MinValueValidator(30), MaxValueValidator(220)],
        help_text="Latidos por minuto (30-220)",
    )

    # Temperatura: 30-45 grados Celsius
    temperatura = models.FloatField(
        "Temperatura (°C)",
        validators=[MinValueValidator(30), MaxValueValidator(45)],
        help_text="Temperatura corporal en grados Celsius (30-45)",
    )

    # Presión Arterial Sistólica: 50-250 mmHg
    pArterialSistolica = models.FloatField(
        "Presión Arterial Sistólica",
        validators=[MinValueValidator(50), MaxValueValidator(250)],
        help_text="Presión arterial sistólica en mmHg (50-250)",
        default=120,
    )

    # Presión Arterial Diastólica: 30-150 mmHg
    pArterialDiastolica = models.FloatField(
        "Presión Arterial Diastólica",
        validators=[MinValueValidator(30), MaxValueValidator(150)],
        help_text="Presión arterial diastólica en mmHg (30-150)",
        default=80,
    )

    # Glicemia: 20-600 mg/dL
    glicemias = models.FloatField(
        "Glicemia (mg/dL)",
        validators=[MinValueValidator(20), MaxValueValidator(600)],
        help_text="Nivel de glucosa en sangre en mg/dL (20-600)",
    )

    fechaHora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Signos Vitales - {self.id_paciente} - {self.fechaHora.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Signos Vitales"
        verbose_name_plural = "Signos Vitales"
        ordering = ["-fechaHora"]
