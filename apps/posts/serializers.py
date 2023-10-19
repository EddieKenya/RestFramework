from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'  
        extra_kwargs = {'author': {'read_only': True}}

    def create(self, validated_data):
        user = self.context.get('request', {}).user

        if user is None:
            raise serializers.ValidationError("User not available in the request context.")

        # Use get method with a default value to avoid KeyError
        data = Post.objects.create(
            author=user,
            bio=validated_data.get('bio', ''),
            pics=validated_data.get('file', None)
        )
        return data

