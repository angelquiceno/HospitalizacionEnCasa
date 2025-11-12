from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.models.Familiar import ClaseFamiliar
from appHospital.serializers.FamiliarSerializer import ClaseFamiliarSerializer


class ClaseFamiliarDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) un familiar específico
    """

    queryset = ClaseFamiliar.objects.all()
    serializer_class = ClaseFamiliarSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de un familiar"""
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente un familiar"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente un familiar"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar un familiar"""
        return self.destroy(request, *args, **kwargs)
