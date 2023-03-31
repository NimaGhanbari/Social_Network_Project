from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()



class Post(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=50)
    avatar = models.ImageField(verbose_name=_('avatar'),blank=True,upload_to="media/")
    user = models.ForeignKey(User, on_delete= models.CASCADE)
    caption = models.TextField(verbose_name=_('caption'),blank=True,max_length=1024,null=True)
    is_active = models.BooleanField(default=True,null=True)
    is_public = models.BooleanField(default=True,null=True)
    create_time = models.DateTimeField(
        verbose_name=_("create time"), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_("update time"), auto_now=True)
    
    class Meta:
        db_table = 'Posts'
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')
          
class Post_File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_IMG = 3
    FILE_TYPES = (
        (FILE_AUDIO,_('audio')),
        (FILE_VIDEO,_('video')),
        (FILE_IMG,_('image'))
    )
    title = models.CharField(_("title"),max_length=50)
    file_type =models.PositiveSmallIntegerField(_("file type"), choices=FILE_TYPES)
    fil = models.FileField(_("file"),upload_to="media/%Y/%m/%d/")
    post = models.ForeignKey('Post',verbose_name=_("Post"), on_delete=models.CASCADE)
    is_enable = models.BooleanField(_("is enable"),default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "files"
        verbose_name = _("file")
        verbose_name_plural = _("files")
        
    def __str__(self):
        return self.title    


class Comment(models.Model):
    user = models.ForeignKey(to=User, on_delete= models.PROTECT)
    post = models.ForeignKey(to=Post,related_name='comments', on_delete=models.CASCADE)
    text = models.TextField(max_length=2048)
    is_approved = models.BooleanField(default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "Comments"
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        


class Like(models.Model):
    user = models.ForeignKey(to=User, on_delete= models.PROTECT)
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=False)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "Likes"
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")



class CommentReply(models.Model):
    parentComment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete= models.PROTECT)
    text = models.TextField(max_length=1048)
    is_approved = models.BooleanField(default=True)
    create_time = models.DateTimeField(_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(_("update time"),auto_now=True)
    
    class Meta:
        db_table = "CommentReplys"
        verbose_name = _("CommentReply")
        verbose_name_plural = _("CommentReplys")