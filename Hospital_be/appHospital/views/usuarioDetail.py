from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appHospital.models.user import ClaseUser
from appHospital.serializers.userSerializer import ClaseUsarioSerializer


class ClaseUserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) un usuario específico
    """

    queryset = ClaseUser.objects.all()
    serializer_class = ClaseUsarioSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de un usuario"""
        token = request.META.get("HTTP_AUTHORIZATION", "")[7:]
        if token:
            token_backend = TokenBackend(algorithm=settings.SIMPLE_JWT["ALGORITHM"])
            valid_data = token_backend.decode(token, verify=False)

            # Verificar que el usuario solo pueda ver su propia información
            if valid_data["user_id"] != kwargs["pk"]:
                return Response(
                    {"detail": "No tiene permiso para ver este usuario"},
                    status=status.HTTP_403_FORBIDDEN,
                )

        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente un usuario"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente un usuario"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar un usuario (soft delete - marcar como inactivo)"""
        instance = self.get_object()
        instance.is_active = False
        instance.save()
        return Response(
            {"detail": "Usuario desactivado exitosamente"},
            status=status.HTTP_204_NO_CONTENT,
        )
