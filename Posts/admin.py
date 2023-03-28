from django.contrib import admin
from .models import Post,Post_File

class FileInLineAdmin(admin.StackedInline):
    model = Post_File
    fields = ['title','fil','is_enable','file_type']
    extra = 0


@admin.register(Post)
class PostFileAdmin(admin.ModelAdmin):
    list_display = ['title','is_active']
    inlines = [FileInLineAdmin]
    
    
