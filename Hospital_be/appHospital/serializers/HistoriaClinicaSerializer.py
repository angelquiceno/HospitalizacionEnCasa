from appHospital.models.HistoriaClinica import ClaseHistoriaClinica
from rest_framework import serializers


class ClaseHistoriaClinicaSerializer(serializers.ModelSerializer):
    # Campos de solo lectura
    nombre_paciente = serializers.CharField(
        source="id_paciente.id_user.nombre", read_only=True
    )
    apellido_paciente = serializers.CharField(
        source="id_paciente.id_user.apellido", read_only=True
    )

    class Meta:
        model = ClaseHistoriaClinica
        fields = (
            "id_HistoriaClinica",
            "id_paciente",
            "sugerencias",
            "diagnostico",
            "entorno",
            "fecha",
            "descripcion",
            "nombre_paciente",
            "apellido_paciente",
        )
        read_only_fields = ("id_HistoriaClinica", "fecha")

    def validate_diagnostico(self, value):
        """Validar que el diagnóstico no esté vacío"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("El diagnóstico no puede estar vacío.")
        return value

    def validate_descripcion(self, value):
        """Validar que la descripción no esté vacía"""
        if not value or value.strip() == "":
            raise serializers.ValidationError("La descripción no puede estar vacía.")
        return value
