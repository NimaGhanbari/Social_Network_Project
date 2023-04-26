from rest_framework import serializers
from .models import Post,Post_File,Comment,CommentReply
from django.contrib.auth import get_user_model
User = get_user_model()

class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = Post_File
        fields = ('title','fil','file_type')
        
    def get_file_type(self,obj):
        return obj.get_file_type_display()   

class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id','title','avatar','caption','is_active','is_public','user')
        
    
        
        
class PostSerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('user','title','caption','is_active','is_public')
        extra_kwargs = {
            'user':{'read_only':True}
        }
        
        
class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('user','text','create_time','update_time')
        #این رید انلی فقط برای ان است که هنگام خوانده شدن از دیتابیس یوزر را بفرستد و برای ذخیره کردندر دیتابیس کاری به یوزر نداشته باشد
        extra_kwargs = {
            'user':{'read_only':True}
        }
        
        
class ParCommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CommentReply
        fields = ('user','text','create_time','update_time')
        #این رید انلی فقط برای ان است که هنگام خوانده شدن از دیتابیس یوزر را بفرستد و برای ذخیره کردندر دیتابیس کاری به یوزر نداشته باشد
        extra_kwargs = {
            'user':{'read_only':True}
        }
        
        