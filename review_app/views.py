from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Review

from .serializers import ReviewCreateSerializer


class ReviewCreateApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        if request.user.is_authenticated:
            request.data['author'] = request.user.pk
            serializer = ReviewCreateSerializer(data=request.data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({'message': 'You must sign in!'})


class ReviewDeleteApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def delete(self, request, review_id):
        review = Review.objects.get(id=review_id)
        review.delete()
        return Response({'message': 'Review deleted!'}, status=status.HTTP_200_OK)




