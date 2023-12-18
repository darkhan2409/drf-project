from rest_framework.serializers import ModelSerializer

from .models import Clinic
from review_app.serializers import ReviewSerializer
from specialist_app.serializers import SpecialistSerializer


class ClinicSerializer(ModelSerializer):
    class Meta:
        model = Clinic
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['reviews'] = ReviewSerializer(instance.reviews.all(), many=True).data
        representation['specialists'] = SpecialistSerializer(instance.specialists.all(), many=True).data
        return representation

