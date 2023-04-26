from django.urls import path
from .views import (PostListView,MyPost,AddPostView,PostSerView,CommentView
                    ,CommentReply,ApiTemperture)

urlpatterns = [
    
    path('list/',PostListView.as_view(), name='Posts-list'),
    path('forme/',MyPost.as_view()),
    path('addpost/',AddPostView.as_view()),
    path('addserpost/',PostSerView.as_view()),
    path('addserpost/<int:pk>/',PostSerView.as_view()),
    path('comment-line/<int:pk>/',CommentView.as_view()),
    path('comment-reply/<int:pk_post>/<int:pk_comment>/',CommentReply.as_view()),
    path('api-temperture/',ApiTemperture.as_view()),
    
]