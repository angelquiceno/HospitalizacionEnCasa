
from appHospital.models.user import ClaseUser
from rest_framework import serializers


class ClaseUsarioSerializer (serializers.ModelSerializer):

    class Meta:
        model= ClaseUser
        fields=('username','password','perfil', 'nombre', 'apellido', 'telefono', 'genero')
    
    def to_representation(self, obj):
        user= ClaseUser.objects.get(id_user=obj.id_user)
        return {
                    'id_user': user.id_user,
                    'username': user.username,
                    'password': user.password,
                    'perfil': user.perfil,
                    'nombre': user.nombre,
                    'apellido': user.apellido,
                    'telefono': user.telefono,
                    'genero': user.genero
                    
                }