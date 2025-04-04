from dataclasses import fields
from appHospital.models.HistoriaClinica import ClaseHistoriaClinica
from rest_framework import serializers

class ClaseHistoriaClinicaSerializer (serializers.ModelSerializer):
    class Meta:
        model=ClaseHistoriaClinica
        fields=('sugerencias','diagnostico','enterno','fecha','descripcion')
