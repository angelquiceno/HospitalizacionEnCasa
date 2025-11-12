from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.models.Paciente import ClasePaciente
from appHospital.serializers.PacienteSerializer import ClasePacienteSerializer


class ClasepacienteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) un paciente específico
    """

    queryset = ClasePaciente.objects.all()
    serializer_class = ClasePacienteSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de un paciente"""
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente un paciente"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente un paciente"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar un paciente"""
        return self.destroy(request, *args, **kwargs)
