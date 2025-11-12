from appHospital.models.user import ClaseUser
from rest_framework import serializers


class ClaseUsarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, min_length=6, style={"input_type": "password"}
    )

    class Meta:
        model = ClaseUser
        fields = (
            "id_user",
            "username",
            "password",
            "perfil",
            "nombre",
            "apellido",
            "telefono",
            "genero",
            "is_active",
        )
        read_only_fields = ("id_user", "is_active")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        """Crear usuario con contraseña hasheada"""
        user = ClaseUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """Actualizar usuario, manejando contraseña si se proporciona"""
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    def to_representation(self, instance):
        """Personalizar la representación de salida"""
        representation = super().to_representation(instance)
        # Nunca incluir la contraseña en la respuesta
        representation.pop("password", None)
        return representation
