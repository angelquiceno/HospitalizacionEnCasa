from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from appHospital.serializers.userSerializer import ClaseUsarioSerializer


class ClaseUserMeView(views.APIView):
    """
    Vista para obtener información del usuario autenticado actual
    """

    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        """Obtener información del usuario actual"""
        serializer = ClaseUsarioSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)
