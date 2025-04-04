from urllib import request
from rest_framework import status, views
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from appHospital.serializers.userSerializer import ClaseUsarioSerializer

class ClaseCrearUsuarioView(views.APIView):


    def post(self, request, *args, **Kwargs):
        VariableUserSerializer=ClaseUsarioSerializer(data=request.data)
        VariableUserSerializer.is_valid(raise_exception=True)
        VariableUserSerializer.save()

        tokenData={
            "username":request.data["username"],
            "password":request.data["password"]
        }

        tokenVariableUserSerializer= TokenObtainPairSerializer(data=tokenData)
        tokenVariableUserSerializer.is_valid(raise_exception=True)

        return Response(tokenVariableUserSerializer.validated_data, status=status.HTTP_201_CREATED)