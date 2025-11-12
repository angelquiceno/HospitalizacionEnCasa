from appHospital.models.SignosVitales import ClaseSignosVitales
from rest_framework import serializers


class ClaseSignosVitalesSerializer(serializers.ModelSerializer):
    # Campos de solo lectura
    nombre_paciente = serializers.CharField(
        source="id_paciente.id_user.nombre", read_only=True
    )
    apellido_paciente = serializers.CharField(
        source="id_paciente.id_user.apellido", read_only=True
    )

    class Meta:
        model = ClaseSignosVitales
        fields = (
            "id_vitales",
            "id_paciente",
            "oximetria",
            "fRespiratoria",
            "fCardiaca",
            "temperatura",
            "pArterialSistolica",
            "pArterialDiastolica",
            "glicemias",
            "fechaHora",
            "nombre_paciente",
            "apellido_paciente",
        )
        read_only_fields = ("id_vitales", "fechaHora")

    def validate(self, data):
        """Validaciones cruzadas de signos vitales"""
        # Validar que la presión sistólica sea mayor que la diastólica
        if "pArterialSistolica" in data and "pArterialDiastolica" in data:
            if data["pArterialSistolica"] <= data["pArterialDiastolica"]:
                raise serializers.ValidationError(
                    "La presión arterial sistólica debe ser mayor que la diastólica."
                )

        return data
