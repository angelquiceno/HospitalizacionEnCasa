from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny

from appHospital.serializers.userSerializer import ClaseUsarioSerializer
from appHospital.models.user import ClaseUser


class ClaseCrearUsuarioView(views.APIView):
    """
    Vista para crear usuarios (POST) y listar todos los usuarios (GET)
    """

    def get_permissions(self):
        """Permitir acceso sin autenticación solo para POST (registro)"""
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request, *args, **kwargs):
        """Listar todos los usuarios"""
        usuarios = ClaseUser.objects.all()
        serializer = ClaseUsarioSerializer(usuarios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """Crear un nuevo usuario y retornar tokens JWT"""
        serializer = ClaseUsarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # Generar tokens JWT para el usuario recién creado
        token_data = {
            "username": request.data["username"],
            "password": request.data["password"],
        }

        token_serializer = TokenObtainPairSerializer(data=token_data)
        token_serializer.is_valid(raise_exception=True)

        return Response(token_serializer.validated_data, status=status.HTTP_201_CREATED)
