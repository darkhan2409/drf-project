from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Record
from clinic_app.models import Clinic
from specialist_app.models import Specialist

from .serializers import RecordSerializer, RecordUpdateSerializer


class RecordApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        record = Record.objects.filter(name=request.user)
        data = RecordSerializer(record, many=True).data
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        clinic_id = request.data['clinic']
        clinic = get_object_or_404(Clinic.objects.all(), pk=clinic_id)
        specialist_id = request.data['specialist']
        specialists = get_object_or_404(Specialist.objects.all(), pk=specialist_id)
        request.data['name'] = request.user.pk
        if specialists in clinic.specialists.all():
            serializer = RecordSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'There are no such specialists in this clinic'}, status=status.HTTP_400_BAD_REQUEST)


class RecordUpdateApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def patch(self, request, record_id):
        clinic_id = request.data['clinic']
        clinic = get_object_or_404(Clinic.objects.all(), pk=clinic_id)
        specialist_id = request.data['specialist']
        specialists = get_object_or_404(Specialist.objects.all(), pk=specialist_id)
        if specialists in clinic.specialists.all():
            record = Record.objects.get(id=record_id)
            serializer = RecordUpdateSerializer(record, request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                data = RecordSerializer(record, many=False).data
                return Response(data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'There are no such specialists in this clinic'}, status=status.HTTP_400_BAD_REQUEST)


class RecordDeleteApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, record_id):
        record = Record.objects.get(id=record_id)
        record.delete()
        return Response({'message': 'Record deleted!'}, status=status.HTTP_200_OK)




