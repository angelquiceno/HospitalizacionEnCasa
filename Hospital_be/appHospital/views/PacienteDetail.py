from django.conf import settings
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.backends import TokenBackend
from rest_framework.permissions import IsAuthenticated
from appHospital.models.Paciente import ClasePaciente
from appHospital.serializers.PacienteSerializer import ClasePacienteSerializer
class ClasepacienteDetail(generics.RetrieveAPIView):
    queryset= ClasePaciente.objects.all()
    serializer_class=ClasePacienteSerializer
    permission_classes =(IsAuthenticated,)
    def get(self, request, *args, **kwargs):
        token = request.META.get('HTTP_AUTHORIZATION')[7:]
        tokenBackend = TokenBackend(algorithm=settings.SIMPLE_JWT['ALGORITHM'])
        valid_data=tokenBackend.decode(token,verify=False)
        if valid_data['id_Paciente'] !=kwargs['pk']:
            stringResponse ={'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED)
        return super().get(request, *args, **kwargs)
