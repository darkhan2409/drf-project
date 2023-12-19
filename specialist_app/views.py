from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Specialist
from .serializers import SpecialistAllSerializer


class SpecialistsApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        specialists = Specialist.objects.all()
        if 'order_by' in request.GET.keys():
            ordering = request.GET.get('order_by')
            specialists = specialists.order_by(ordering)
        if 'search' in request.GET.keys():
            search = request.GET.get('search')
            specialists = specialists.filter(speciality__contains=search)
        data = SpecialistAllSerializer(specialists, many=True).data
        return Response(data, status=status.HTTP_200_OK)
