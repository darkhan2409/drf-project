from rest_framework.serializers import ModelSerializer
from .models import Specialist
from clinic_app.models import Clinic


class SpecialistSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'


class ClinicsSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = ['id', 'title']


class SpecialistAllSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['clinic'] = ClinicsSerializer(instance.clinic).data
        return representation


