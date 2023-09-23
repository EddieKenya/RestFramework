from django.urls import path
from.import views

urlpatterns = [
    path('register/', views.CreateUser.as_view()),
    path('profile/', views.RetrieveUser.as_view()),
    path('list/', views.UsersList.as_view()),
]