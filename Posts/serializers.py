from rest_framework import serializers
from .models import Post,Post_File


class FileSerializer(serializers.ModelSerializer):
    file_type = serializers.SerializerMethodField()
    class Meta:
        model = Post_File
        fields = ('title','fil','file_type')
        
    def get_file_type(self,obj):
        return obj.get_file_type_display()   


class PostsSerializer(serializers.ModelSerializer):
    #file_set = FileSerializer(many= True)
    class Meta:
        model = Post
        fields = ('id','title','avatar','caption','is_active','is_public')
        
        
class PostSerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = ('user','title','caption','is_active','is_public')
        extra_kwargs = {
            'user':{'read_only':True}
        }