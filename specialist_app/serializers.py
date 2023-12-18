from rest_framework.serializers import ModelSerializer
from .models import Specialist


class SpecialistSerializer(ModelSerializer):
    class Meta:
        model = Specialist
        fields = '__all__'




