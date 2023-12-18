from .models import Patient
from rest_framework.serializers import ModelSerializer


class SignUpSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['username', 'password', 'birth_date', 'region', 'phone', 'email']

    def create(self, validated_data):
        patient = Patient.objects.create(**validated_data)
        patient.set_password(validated_data['password'])
        patient.save()
        return patient


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['username', 'birth_date', 'region', 'phone', 'email']


class ProfileUpdateSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['birth_date', 'region', 'phone', 'email']

