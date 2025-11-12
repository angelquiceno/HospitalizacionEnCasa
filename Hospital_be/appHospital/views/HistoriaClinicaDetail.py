from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.models.HistoriaClinica import ClaseHistoriaClinica
from appHospital.serializers.HistoriaClinicaSerializer import (
    ClaseHistoriaClinicaSerializer,
)


class ClaseHistoriaClinicaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) una historia clínica específica
    """

    queryset = ClaseHistoriaClinica.objects.all()
    serializer_class = ClaseHistoriaClinicaSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de una historia clínica"""
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente una historia clínica"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente una historia clínica"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar una historia clínica"""
        return self.destroy(request, *args, **kwargs)


class ClasePacienteHistoriasView(views.APIView):
    """
    Vista para obtener todas las historias clínicas de un paciente específico
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, paciente_id):
        """Listar todas las historias clínicas de un paciente"""
        historias = ClaseHistoriaClinica.objects.filter(id_paciente=paciente_id)
        serializer = ClaseHistoriaClinicaSerializer(historias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
