from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from appHospital.serializers.HistoriaClinicaSerializer import (
    ClaseHistoriaClinicaSerializer,
)
from appHospital.models.HistoriaClinica import ClaseHistoriaClinica


class ClaseCrearHistoriaClinicaView(views.APIView):
    """
    Vista para crear historias clínicas (POST) y listar todas las historias (GET)
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Listar todas las historias clínicas"""
        historias = ClaseHistoriaClinica.objects.all()
        serializer = ClaseHistoriaClinicaSerializer(historias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crear una nueva historia clínica"""
        serializer = ClaseHistoriaClinicaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
