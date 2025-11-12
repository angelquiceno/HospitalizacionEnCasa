from django.db import models
from .user import ClaseUser
from .Paciente import ClasePaciente


class ClaseFamiliar(models.Model):
    PARENTEZCO_CHOICES = [
        ("padre", "Padre"),
        ("madre", "Madre"),
        ("hijo", "Hijo/a"),
        ("hermano", "Hermano/a"),
        ("conyuge", "Cónyuge"),
        ("abuelo", "Abuelo/a"),
        ("nieto", "Nieto/a"),
        ("tio", "Tío/a"),
        ("sobrino", "Sobrino/a"),
        ("primo", "Primo/a"),
        ("otro", "Otro"),
    ]

    id_Familiar = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(
        ClaseUser, related_name="Familiar", on_delete=models.CASCADE
    )
    id_Paciente = models.ForeignKey(
        ClasePaciente, related_name="Familiar", on_delete=models.CASCADE
    )
    email = models.EmailField("Email", max_length=100)
    parentezco = models.CharField(
        "Parentezco", max_length=45, choices=PARENTEZCO_CHOICES
    )

    def __str__(self):
        return f"{self.id_user.nombre} {self.id_user.apellido} - {self.get_parentezco_display()}"

    class Meta:
        verbose_name = "Familiar"
        verbose_name_plural = "Familiares"
