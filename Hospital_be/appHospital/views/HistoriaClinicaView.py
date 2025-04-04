from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.HistoriaClinicaSerializer import ClaseHistoriaClinicaSerializer

class ClaseCrearHistoriaClinicaView(views.APIView):
    def post(self,request):
        VariableHistoriaClinicaSerializer=ClaseHistoriaClinicaSerializer(data=request.data)
        if VariableHistoriaClinicaSerializer.is_valid():
            VariableHistoriaClinicaSerializer.save()
            return Response(VariableHistoriaClinicaSerializer.data, status=status.HTTP_201_CREATED)
        return Response(VariableHistoriaClinicaSerializer.errors, status=status.HTTP_400_BAD_REQUEST)