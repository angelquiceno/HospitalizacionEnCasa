from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.FamiliarSerializer import ClaseFamiliarSerializer

class ClaseCrearFamiliarView(views.APIView):
    def post(self,request):
        VariableFamiliarSerializer=ClaseFamiliarSerializer(data=request.data)
        if VariableFamiliarSerializer.is_valid():
            VariableFamiliarSerializer.save()
            return Response(VariableFamiliarSerializer.data, status=status.HTTP_201_CREATED)
        return Response(VariableFamiliarSerializer.errors, status=status.HTTP_400_BAD_REQUEST)