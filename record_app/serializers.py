from rest_framework.serializers import ModelSerializer
from .models import Record

from clinic_app.models import Clinic
from specialist_app.models import Specialist


class ClinicRecordSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['title']


class SpecialistRecordSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = ['name', 'speciality', 'price']


class RecordSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clinic'] = ClinicRecordSerializer(instance.clinic).data
        representation['specialist'] = SpecialistRecordSerializer(instance.specialist).data
        return representation


class RecordUpdateSerializer(ModelSerializer):
    class Meta:
        model = Record
        fields = ['date', 'time']


