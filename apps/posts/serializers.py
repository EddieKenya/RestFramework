from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'  # Include 'likes_count' in the fields

    def get_likes_count(self, obj):
        return obj.likes.count()

    def create(self, validated_data):
        request = self.context.get('request')
        author = request.user

        post = Post.objects.create(author=author, **validated_data)
        return post
