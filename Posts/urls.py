from django.urls import path
from .views import PostListView,PostForMe,AddPostView,PostSerView,CommentView

urlpatterns = [
    
    path('list/',PostListView.as_view(), name='Posts-list'),
    path('forme/',PostForMe.as_view()),
    path('addpost/',AddPostView.as_view()),
    path('addserpost/',PostSerView.as_view()),
    path('addserpost/<int:pk>/',PostSerView.as_view()),
    path('comment-lise/<int:pk>/',CommentView.as_view()),
    
]