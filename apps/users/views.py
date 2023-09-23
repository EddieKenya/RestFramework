from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import RegisterUserSerializer, UserListSerializer
from rest_framework import permissions, status
from django.contrib.auth import get_user_model
from rest_framework import generics

User= get_user_model()


        
    
class CreateUser(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        serializers = RegisterUserSerializer(data=data)
        if not serializers.is_valid():
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        user = serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)
    
        
class RetrieveUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = RegisterUserSerializer(user)

        return Response(serializer.data, status=status.HTTP_200_OK)
    

class UsersList(generics.ListAPIView):
    queryset= User.objects.all()
    serializer_class = UserListSerializer
