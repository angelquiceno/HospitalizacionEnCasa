from dataclasses import fields
from appHospital.models.PersonalSalud import clasePersonalSalud
from rest_framework import serializers

class ClasePersonalSaludSerializer (serializers.ModelSerializer):
    class Meta:
        model=clasePersonalSalud
        fields=('id_user','rol','especialidad')
    def to_representation(self, obj):
        Psalud= clasePersonalSalud.objects.get(id_PersonalSalud=obj.id_PersonalSalud)
        return {
                'id_PersonalSalud': Psalud.id_PersonalSalud,
                'id_user': Psalud.id_user,
                'rol': Psalud.rol,
                'especialidad': Psalud.especialidad                
                }