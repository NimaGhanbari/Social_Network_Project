from django.contrib import admin
from .models import Post,Post_File,Comment,Like

class FileInLineAdmin(admin.StackedInline):
    model = Post_File
    fields = ['id','title','fil','is_enable','file_type']
    extra = 0


class CommentInLineAdmin(admin.StackedInline):
    model = Comment
    fields = ['id','text','user']
    extra = 0

class LikeInLineAdmin(admin.StackedInline):
    model = Like
    fields = ['id','user','is_liked']
    extra = 0


@admin.register(Post)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active','user','create_time']
    list_filter = ['create_time']
    search_fields = ['title']
    inlines = [FileInLineAdmin,CommentInLineAdmin,LikeInLineAdmin]
    
    

    
    
