from .serializers import ListUserSerializer, ListRequestSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Friendship
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView

from django.db.models import Q


class UserListView(APIView):
    def get(self, request):
        users = User.objects.filter(is_staff=False, is_active=True)
        serialized = ListUserSerializer(users, many=True, context={'request': request})
        return Response(serialized.data)


class request_view(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user_to = get_object_or_404(User, pk=pk)
        Friendship.objects.get_or_create(
            request_from=request.user, request_to=user_to, is_accepted=False)
        return Response({'title': 'Your request has been successfully sent'}, status=status.HTTP_200_OK)


class RequestListForMe(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        requests = Friendship.objects.filter(
            request_to=request.user, is_accepted=False)
        users = [fr.request_from for fr in requests]
        serialized = ListUserSerializer(users, many=True, context={'request': request})
        return Response(serialized.data)


class AcceptedView(APIView):

    def post(self, request):

        user_id = request.data.get('user_id')
        user_from = get_object_or_404(User,pk=user_id)
        friendship = get_object_or_404(
            Friendship, request_from=user_from, request_to=request.user, is_accepted=False)
        friendship.is_accepted = True
        friendship.save()
        return Response({'title': 'connected'}, status=status.HTTP_202_ACCEPTED)


class FriendsConnectView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        #connections = Friendship.objects.filter(request_from=request.user,is_accepted=True)
        #connections += Friendship.objects.filter(request_to=request.user,is_accepted=True)
        
        connections = Friendship.objects.filter(
            Q(request_from=request.user)|Q(request_to=request.user),
            is_accepted=True,
        )
        users = [fr.request_from for fr in connections]
        serialized = ListUserSerializer(users, many=True, context={'request': request})
        return Response(serialized.data)
        
        
        
        