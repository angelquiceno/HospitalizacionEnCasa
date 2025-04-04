from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.SignosVitalesSerliazer import ClaseSignosVitalesSerializer

class ClaseCrearSignosVitalesView(views.APIView):
    def post(self,request):
        VariableSignosVitalesSerializer=ClaseSignosVitalesSerializer(data=request.data)
        if VariableSignosVitalesSerializer.is_valid():
            VariableSignosVitalesSerializer.save()
            return Response(VariableSignosVitalesSerializer.data, status=status.HTTP_201_CREATED)
        return Response(VariableSignosVitalesSerializer.errors, status=status.HTTP_400_BAD_REQUEST)