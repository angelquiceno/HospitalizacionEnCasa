from dataclasses import fields
from appHospital.models.Familiar import ClaseFamiliar
from rest_framework import serializers

class ClaseFamiliarSerializer (serializers.ModelSerializer):
    class Meta:
        model=ClaseFamiliar
        fields=('email','parentezco')

