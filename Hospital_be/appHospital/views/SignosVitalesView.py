from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from appHospital.serializers.SignosVitalesSerliazer import ClaseSignosVitalesSerializer
from appHospital.models.SignosVitales import ClaseSignosVitales


class ClaseCrearSignosVitalesView(views.APIView):
    """
    Vista para crear signos vitales (POST) y listar todos los signos (GET)
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Listar todos los signos vitales"""
        signos = ClaseSignosVitales.objects.all()
        serializer = ClaseSignosVitalesSerializer(signos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crear un nuevo registro de signos vitales"""
        serializer = ClaseSignosVitalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
