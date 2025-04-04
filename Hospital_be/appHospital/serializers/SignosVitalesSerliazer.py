from dataclasses import fields
from appHospital.models.SignosVitales import ClaseSignosVitales
from rest_framework import serializers

class ClaseSignosVitalesSerializer (serializers.ModelSerializer):
    class Meta:
        model=ClaseSignosVitales
        fields=('oximetria','fRespiratoria','fCardiaca','temperatura','pArterial','glicemias','fechaHora')
