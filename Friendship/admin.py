from django.contrib import admin
from .models import Friendship

@admin.register(Friendship)
class FriendshipAdmin(admin.ModelAdmin):
    list_display = ['id','request_from','request_to','is_accepted']
    
    def has_add_permission(self, request,obj=None):
        return False
    def has_change_permission(self, request,obj=None):
        return False
    def has_delete_permission(self, request,obj=None):
        return False
    