from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class RegisterUserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name','last_name','email','username','password','date_joined')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(

            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            username = validated_data['username'],
            password = validated_data['password'],
        )


        return user

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

