from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from appHospital.serializers.PacienteSerializer import ClasePacienteSerializer
from appHospital.models.Paciente import ClasePaciente


class ClaseCrearPacienteView(views.APIView):
    """
    Vista para crear pacientes (POST) y listar todos los pacientes (GET)
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request):
        """Listar todos los pacientes"""
        pacientes = ClasePaciente.objects.all()
        serializer = ClasePacienteSerializer(pacientes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        """Crear un nuevo paciente"""
        serializer = ClasePacienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
