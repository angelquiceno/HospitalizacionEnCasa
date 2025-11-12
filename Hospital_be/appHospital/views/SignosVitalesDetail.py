from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.models.SignosVitales import ClaseSignosVitales
from appHospital.serializers.SignosVitalesSerliazer import ClaseSignosVitalesSerializer


class ClaseSignosVitalesDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para obtener (GET), actualizar (PUT/PATCH) y eliminar (DELETE) signos vitales específicos
    """

    queryset = ClaseSignosVitales.objects.all()
    serializer_class = ClaseSignosVitalesSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener detalles de signos vitales"""
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """Actualizar completamente signos vitales"""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """Actualizar parcialmente signos vitales"""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """Eliminar signos vitales"""
        return self.destroy(request, *args, **kwargs)


class ClasePacienteSignosView(views.APIView):
    """
    Vista para obtener todos los signos vitales de un paciente específico
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, paciente_id):
        """Listar todos los signos vitales de un paciente"""
        signos = ClaseSignosVitales.objects.filter(id_paciente=paciente_id)
        serializer = ClaseSignosVitalesSerializer(signos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ClasePacienteUltimoSignoView(views.APIView):
    """
    Vista para obtener el último registro de signos vitales de un paciente
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, paciente_id):
        """Obtener el último registro de signos vitales de un paciente"""
        try:
            ultimo_signo = ClaseSignosVitales.objects.filter(
                id_paciente=paciente_id
            ).latest("fechaHora")
            serializer = ClaseSignosVitalesSerializer(ultimo_signo)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ClaseSignosVitales.DoesNotExist:
            return Response(
                {"detail": "No se encontraron signos vitales para este paciente"},
                status=status.HTTP_404_NOT_FOUND,
            )
