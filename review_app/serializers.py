from rest_framework.serializers import ModelSerializer
from .models import Review

from patient_app.models import Patient


class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'created_at']

########################################


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'username']


class ReviewCreateSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['text', 'clinic', 'author']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = AuthorSerializer(instance.author).data
        return representation

