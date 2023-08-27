from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from.models import Post
from.serializers import PostSerializer
from.permissions import IsAuthorOrReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]



class PostRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]



class CreatePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        serializer = PostSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save(author= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    
class LikePost(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            user = request.user
            if user in post.likes.all():
                post.likes.remove(user)
                return Response({'message': 'Post unliked'}, status=status.HTTP_200_OK)
            else:
                post.likes.add(user)
                return Response({'message': 'Post liked'}, status=status.HTTP_200_OK)

        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)

