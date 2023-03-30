from django.contrib import admin
from .models import Post,Post_File

class FileInLineAdmin(admin.StackedInline):
    model = Post_File
    fields = ['id','title','fil','is_enable','file_type']
    extra = 0


@admin.register(Post)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ['id','title','is_active','user','create_time']
    list_filter = ['create_time']
    search_fields = ['title']
    inlines = [FileInLineAdmin]
    
    
