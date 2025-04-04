from dataclasses import fields
from appHospital.models.Paciente import ClasePaciente
from rest_framework import serializers

class ClasePacienteSerializer (serializers.ModelSerializer):
    class Meta:
        model=ClasePaciente
        fields=('id_PersonalSalud','id_user','direccion','ciudad', 'fecha_nacimiento')
    def to_representation(self, obj):
        paciente= ClasePaciente.objects.get(id_Paciente=obj.id_Paciente)
        return {
                'id_Paciente': paciente.id_Paciente,
                'id_PersonalSalud': paciente.id_PersonalSalud,
                'id_user': paciente.id_user,
                'direccion': paciente.direccion,
                'ciudad': paciente.ciudad,
                'fecha_nacimiento': paciente.fecha_nacimiento                   
                }


    