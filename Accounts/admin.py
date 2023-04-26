from django.contrib import admin
from .models import Profile,Country




@admin.register(Profile)
class profileAdmin(admin.ModelAdmin):
    list_display = ['id','user','avatar','phone_number','create_time']
    
    
@admin.register(Country)
class ContryAdmin(admin.ModelAdmin):
    list_display = ['id','name','abbr','is_enable']