from django.urls import path
from .views import PostRetrieveUpdateDeleteView, PostList, LikePost, CreatePost

urlpatterns = [
    path('create/', CreatePost.as_view(), name='post-create'),
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-retrieve-update-delete'),
    path('posts/<int:post_id>/like/', LikePost.as_view(), name='like-post'),
]
