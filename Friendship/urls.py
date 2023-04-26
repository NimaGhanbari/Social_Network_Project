from django.urls import path
from .views import (UserListView,request_view,RequestListForMe
                    ,AcceptedView,FriendsConnectView)

urlpatterns = [
    
    path('user-list/',UserListView.as_view(), name='user-list'),
    path('relative/<int:pk>/',request_view.as_view(),name='send-request'),
    path('reqlist/',RequestListForMe.as_view(),name= 'request-list'),
    path('accepted/',AcceptedView.as_view(),name= 'request-accepted'),
    path('friend-connections/',FriendsConnectView.as_view(),name= 'friend-connections'),
]