from django.contrib.auth import login, logout, authenticate

from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .serializers import SignUpSerializer, ProfileSerializer, ProfileUpdateSerializer


class SignUpApiView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {
                'message': 'Registration done!'
            }
            return Response(context, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SignInApiView(APIView):
    permission_classes = [AllowAny, ]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            data = {'message': 'Welcome!'}
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = {'message': 'Username or/and Password is not valid!'}
            return Response(data, status=status.HTTP_403_FORBIDDEN)


class SignOutApiView(APIView):
    def get(self, request):
        logout(request)
        return Response({'message': 'You have logged out successfully'}, status=status.HTTP_200_OK)


class ProfileApiView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        data = ProfileSerializer(request.user).data
        return Response(data, status=status.HTTP_200_OK)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response({'message': 'Patient is deleted!'}, status=status.HTTP_200_OK)

    def patch(self, request):
        user = request.user
        serializer = ProfileUpdateSerializer(user, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data = ProfileSerializer(user).data
            return Response(data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

