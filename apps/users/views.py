from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from.serializers import RegisterUserSerializer
from rest_framework import permissions, status
from django.contrib.auth import get_user_model

User= get_user_model()

# Create your views here.

# class CreateUser(APIView):
#     permission_classes = [permissions.AllowAny]
#     def post(self, request):
#         username= request.data['username']
#         first_name= request.data['first_name']
#         last_name= request.data['last_name']
#         email= request.data['email']
#         password= request.data['password']
#         user = User.objects.create_user(username, first_name, last_name, email, password)
#         user = RegisterUserSerializer(user)

#         return Response(user.data, status.HTTP_201_CREATED)
        
    
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
