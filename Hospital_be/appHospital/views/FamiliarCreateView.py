from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from appHospital.serializers.FamiliarSerializer import ClaseFamiliarSerializer
from appHospital.models.Familiar import ClaseFamiliar


class ClaseCrearFamiliarView(views.APIView):
    """
    Vista para crear familiares (POST) y listar todos los familiares (GET)
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Listar todos los familiares"""
        familiares = ClaseFamiliar.objects.all()
        serializer = ClaseFamiliarSerializer(familiares, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crear un nuevo familiar"""
        serializer = ClaseFamiliarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
