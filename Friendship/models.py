from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
User = get_user_model()

class Friendship(models.Model):
    request_from = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='friend_request_from')
    request_to = models.ForeignKey(to=User, on_delete=models.CASCADE,related_name='friend_request_to')
    is_accepted = models.BooleanField(default=False)
    create_time = models.DateTimeField(
        verbose_name=_("create time"), auto_now_add=True)
    update_time = models.DateTimeField(
        verbose_name=_("update time"), auto_now=True)
    
    class Meta:
        verbose_name = 'Friendship'
        verbose_name_plural = 'Friendships'
        unique_together = ('request_from','request_to')
        
    