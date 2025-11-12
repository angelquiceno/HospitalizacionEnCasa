from appHospital.models.PersonalSalud import clasePersonalSalud
from appHospital.serializers.userSerializer import ClaseUsarioSerializer
from rest_framework import serializers


class ClasePersonalSaludSerializer(serializers.ModelSerializer):
    # Campo anidado para mostrar información del usuario
    usuario = ClaseUsarioSerializer(source="id_user", read_only=True)

    class Meta:
        model = clasePersonalSalud
        fields = ("id_PersonalSalud", "id_user", "rol", "especialidad", "usuario")
        read_only_fields = ("id_PersonalSalud",)

    def validate_especialidad(self, value):
        """Validar que la especialidad no esté vacía"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("La especialidad no puede estar vacía.")
        return value
