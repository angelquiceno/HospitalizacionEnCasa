from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.PacienteSerializer import ClasePacienteSerializer

class ClaseCrearPacienteView(views.APIView):
    def post(self,request):
        VariablePacienteSerializer=ClasePacienteSerializer(data=request.data)
        if VariablePacienteSerializer.is_valid():
            VariablePacienteSerializer.save()
            return Response(VariablePacienteSerializer.data, status=status.HTTP_201_CREATED)
        return Response(VariablePacienteSerializer.errors, status=status.HTTP_400_BAD_REQUEST)

