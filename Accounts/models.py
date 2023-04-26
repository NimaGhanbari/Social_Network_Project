from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

class Country(models.Model):
    name = models.CharField(max_length=62)
    abbr = models.CharField(max_length=6)
    is_enable = models.BooleanField(default=True)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)
    
    class Meta:
        db_table = "Countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")
        
    def __str__(self):
        return self.name
    


class Profile(models.Model):
    user = models.OneToOneField(to=settings.AUTH_USER_MODEL,related_name='profiles', on_delete= models.CASCADE)
    avatar = models.ImageField(verbose_name=_("avatar"),upload_to='Profiles/',blank=True)
    bio = models.TextField(verbose_name=_("bio"),blank=True,null=True)
    phone_number = models.BigIntegerField(verbose_name=_("phone number"),blank=True,null=True)
    country =  models.ForeignKey(Country, on_delete= models.CASCADE,null=True)
    create_time = models.DateTimeField(verbose_name=_("create time"),auto_now_add=True)
    update_time = models.DateTimeField(verbose_name=_("update time"),auto_now=True)
    
    
class Device(models.Model):
    WEB = 1
    IOS = 2
    ANDROID = 3
    PC = 4
    DEVICE_TYPE_CHOICE =(
        (WEB,'web'),
        (IOS,'ios'),
        (ANDROID,'android'),
        (PC,'pc')
    )  
    
    #این ریلیتد نیم به خاطر ان است که هنگامی که می خواهیم دیوایس های یک یوزر را گت کنیم باید به صورت زیر بنویسیم
    #user.devices.all()
    #اگر ریلیتد نیم را ننویسیم خود جنگو به صورت دیفالت به شکل زیر میگیرد
    #user.devices_set.all()
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL,related_name='devices', on_delete=models.CASCADE)
    device_uuid = models.UUIDField(_('Device UUID'),null = True)
    last_login = models.DateTimeField(_('last login date'),null= True)
    device_type = models.PositiveSmallIntegerField(choices= DEVICE_TYPE_CHOICE,default=WEB)
    device_os = models.CharField(_('device os'),max_length = 20,blank=True)
    device_model = models.CharField(_('device model'),max_length= 50,blank = True)
    app_version = models.CharField(_('app version'),max_length= 20,blank = True)
    created_time = models.DateTimeField(auto_now_add=True)

