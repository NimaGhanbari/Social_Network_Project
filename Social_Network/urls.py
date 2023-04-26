from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/account/',include('Accounts.urls')),
    path('api/post/',include('Posts.urls')),
    path('api/friendship/',include('Friendship.urls')),
]

#urlpatterns += static('/media',document_root = settings.MEDIA_ROOT)