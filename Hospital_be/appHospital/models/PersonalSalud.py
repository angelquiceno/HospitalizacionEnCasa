from django.db import models
from .user import ClaseUser


class clasePersonalSalud(models.Model):
    ROL_CHOICES = [
        ("medico", "Médico"),
        ("enfermero", "Enfermero/a"),
        ("terapeuta", "Terapeuta"),
        ("auxiliar", "Auxiliar de Enfermería"),
        ("fisioterapeuta", "Fisioterapeuta"),
        ("nutricionista", "Nutricionista"),
        ("psicologo", "Psicólogo/a"),
    ]

    id_PersonalSalud = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        ClaseUser, related_name="PersonalSalud", on_delete=models.CASCADE
    )
    rol = models.CharField("Rol", max_length=45, choices=ROL_CHOICES)
    especialidad = models.CharField("Especialidad", max_length=100)

    def __str__(self):
        return (
            f"{self.get_rol_display()} - {self.id_user.nombre} {self.id_user.apellido}"
        )

    class Meta:
        verbose_name = "Personal de Salud"
        verbose_name_plural = "Personal de Salud"
