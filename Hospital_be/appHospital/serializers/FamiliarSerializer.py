from appHospital.models.Familiar import ClaseFamiliar
from appHospital.serializers.userSerializer import ClaseUsarioSerializer
from rest_framework import serializers


class ClaseFamiliarSerializer(serializers.ModelSerializer):
    # Campos anidados para mostrar información completa
    usuario = ClaseUsarioSerializer(source="id_user", read_only=True)
    nombre_paciente = serializers.CharField(
        source="id_Paciente.id_user.nombre", read_only=True
    )
    apellido_paciente = serializers.CharField(
        source="id_Paciente.id_user.apellido", read_only=True
    )

    class Meta:
        model = ClaseFamiliar
        fields = (
            "id_Familiar",
            "id_user",
            "id_Paciente",
            "email",
            "parentezco",
            "usuario",
            "nombre_paciente",
            "apellido_paciente",
        )
        read_only_fields = ("id_Familiar",)

    def validate_email(self, value):
        """Validar formato de email"""
        if not value or "@" not in value:
            raise serializers.ValidationError("Debe proporcionar un email válido.")
        return value.lower()
