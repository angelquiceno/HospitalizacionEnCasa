from urllib import request
from rest_framework import status, views
from rest_framework.response import Response

from appHospital.serializers.PersonalSaludSerializer import ClasePersonalSaludSerializer

class ClaseCrearPersonalSaludView(views.APIView):
    def post(self,request):
        VariablePersonalSaludSerializer=ClasePersonalSaludSerializer(data=request.data)
        if VariablePersonalSaludSerializer.is_valid():
            VariablePersonalSaludSerializer.save()
            return Response(VariablePersonalSaludSerializer.data, status=status.HTTP_201_CREATED)
        return Response(VariablePersonalSaludSerializer.errors, status=status.HTTP_400_BAD_REQUEST)