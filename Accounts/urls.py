from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RejisterView,create_user_view,SeeProfoleView







urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RejisterView.as_view(),name='register_view'),
    path('create_user/',create_user_view.as_view()),
    path('see-profile/',SeeProfoleView.as_view()),
    #path("token/", EmailTokenObtainPairView.as_view(), name="token_obtain_pair"),
    #path("refresh/", TokenRefreshView.as_view(), name="token_refresh"),  
]