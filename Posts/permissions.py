from rest_framework.permissions import BasePermission
from Friendship.models import Friendship
from django.db.models import Q
from rest_framework.permissions import SAFE_METHODS

class IsFriendship(BasePermission):

    def has_object_permission(self, request, view, obj):
        User = obj.user
        connections = Friendship.objects.filter(
            Q(request_from=User) & Q(request_to=request.user) & Q(is_accepted=True) | 
            Q(request_from=request.user) & Q(request_to=User) & Q(is_accepted=True)

        )
        if connections is None:
            return False
        return True

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        print('1')
    def has_object_permission(self, request, view, obj):
        print('159')
        if request.method == SAFE_METHODS:
            return True
        return request.user == obj.user
            