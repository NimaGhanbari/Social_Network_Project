from django.contrib import admin
from .models import Post,Post_File,Comment,Like,CommentReply
from nested_admin import NestedTabularInline, NestedModelAdmin

class FileInLineAdmin(NestedTabularInline):
    model = Post_File
    fields = ['id','title','fil','is_enable','file_type']
    extra = 0

class ParCommentInLineAdmin(NestedTabularInline):
    model = CommentReply
    fields = ['id','text','user']
    extra = 0

class CommentInLineAdmin(NestedTabularInline):
    model = Comment
    fields = ['id','text','user']
    extra = 0
    inlines = [ParCommentInLineAdmin]



class LikeInLineAdmin(NestedTabularInline):
    model = Like
    fields = ['id','user','is_liked']
    extra = 0


@admin.register(Post)
class PostFileAdmin(NestedModelAdmin):
    list_display = ['id','title','is_active','user','create_time']
    list_filter = ['create_time']
    search_fields = ['title']
    inlines = [FileInLineAdmin,CommentInLineAdmin,LikeInLineAdmin]
    
    

    
    
