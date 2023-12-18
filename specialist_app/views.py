from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Specialist
from .serializers import SpecialistSerializer


class SpecialistsApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        specialists = Specialist.objects.all()
        data = SpecialistSerializer(specialists, many=True).data
        return Response(data, status=status.HTTP_200_OK)
