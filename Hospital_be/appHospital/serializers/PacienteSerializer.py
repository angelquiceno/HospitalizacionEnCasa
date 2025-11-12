from appHospital.models.Paciente import ClasePaciente
from appHospital.serializers.userSerializer import ClaseUsarioSerializer
from rest_framework import serializers


class ClasePacienteSerializer(serializers.ModelSerializer):
    # Campos anidados para mostrar información completa
    usuario = ClaseUsarioSerializer(source="id_user", read_only=True)
    nombre_personal = serializers.CharField(
        source="id_PersonalSalud.id_user.nombre", read_only=True
    )
    apellido_personal = serializers.CharField(
        source="id_PersonalSalud.id_user.apellido", read_only=True
    )

    class Meta:
        model = ClasePaciente
        fields = (
            "id_Paciente",
            "id_PersonalSalud",
            "id_user",
            "direccion",
            "ciudad",
            "fecha_nacimiento",
            "usuario",
            "nombre_personal",
            "apellido_personal",
        )
        read_only_fields = ("id_Paciente",)

    def validate_direccion(self, value):
        """Validar que la dirección no esté vacía"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("La dirección no puede estar vacía.")
        return value

    def validate_ciudad(self, value):
        """Validar que la ciudad no esté vacía"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("La ciudad no puede estar vacía.")
        return value
