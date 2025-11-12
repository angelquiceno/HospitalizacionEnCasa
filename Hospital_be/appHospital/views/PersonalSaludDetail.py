from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.models.PersonalSalud import clasePersonalSalud
from appHospital.serializers.PersonalSaludSerializer import ClasePersonalSaludSerializer


class ClasePersonalSaludDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) un personal de salud específico
    """

    queryset = clasePersonalSalud.objects.all()
    serializer_class = ClasePersonalSaludSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de un personal de salud"""
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente un personal de salud"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente un personal de salud"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar un personal de salud"""
        return self.destroy(request, *args, **kwargs)
