from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import Friendship
from Accounts.models import Profile

class ListUserSerializer(serializers.ModelSerializer):
    #avatar = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','username']
    
    def get_avatar(self,instance):
        if hasattr(instance, 'profile') and instance.profile.avatar:
            return instance.profile.avatar.url
    
        return "ssas"
    
    
    
class ListRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Friendship
        fields = ['id','request_from']