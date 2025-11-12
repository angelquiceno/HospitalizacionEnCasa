from django.db import models
from django.core.exceptions import ValidationError
from datetime import date
from .user import ClaseUser
from .PersonalSalud import clasePersonalSalud


def validar_edad(fecha_nacimiento):
    """Valida que el paciente tenga una edad razonable (0-120 años)"""
    hoy = date.today()
    edad = (
        hoy.year
        - fecha_nacimiento.year
        - ((hoy.month, hoy.day) < (fecha_nacimiento.month, fecha_nacimiento.day))
    )
    if edad < 0 or edad > 120:
        raise ValidationError("La edad del paciente debe estar entre 0 y 120 años.")
    if fecha_nacimiento > hoy:
        raise ValidationError("La fecha de nacimiento no puede ser futura.")


class ClasePaciente(models.Model):
    id_Paciente = models.AutoField(primary_key=True)
    id_PersonalSalud = models.ForeignKey(
        clasePersonalSalud, related_name="Paciente", on_delete=models.CASCADE
    )
    id_user = models.ForeignKey(
        ClaseUser, related_name="Paciente", on_delete=models.CASCADE
    )
    direccion = models.CharField("Direccion", max_length=200)
    ciudad = models.CharField("Ciudad", max_length=100)
    fecha_nacimiento = models.DateField(validators=[validar_edad])

    def __str__(self):
        return f"Paciente: {self.id_user.nombre} {self.id_user.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"
