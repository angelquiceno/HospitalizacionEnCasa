from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from appHospital.serializers.PersonalSaludSerializer import ClasePersonalSaludSerializer
from appHospital.models.PersonalSalud import clasePersonalSalud


class ClaseCrearPersonalSaludView(views.APIView):
    """
    Vista para crear personal de salud (POST) y listar todo el personal (GET)
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Listar todo el personal de salud"""
        personal = clasePersonalSalud.objects.all()
        serializer = ClasePersonalSaludSerializer(personal, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crear un nuevo personal de salud"""
        serializer = ClasePersonalSaludSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
