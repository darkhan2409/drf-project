from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from .models import Clinic

from .serializers import ClinicSerializer


class ClinicApiView(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request):
        clinic = Clinic.objects.all()
        if 'order_by' in request.GET.keys():
            ordering = request.GET.get('order_by')
            clinic = clinic.order_by(ordering)
        if 'search' in request.GET.keys():
            search = request.GET.get('search')
            clinic = clinic.filter(title__contains=search).union(clinic.filter(location__contains=search))
        data = ClinicSerializer(instance=clinic, many=True).data
        return Response(data, status=status.HTTP_200_OK)

