from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model 
from django.core.cache import cache

from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

import mailtrap as mt
import smtplib
from email.message import EmailMessage
from secrets import compare_digest

from .models import Profile
from .serializers import ProfileSerializer

import random

User = get_user_model()


def send_mail(email_r, code_r):
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_HOST_USER = 'nimadfm1400@gmail.com'
    EMAIL_PORT_SSL = 465
    EMAIL_HOST_PASSWORD = 'eillarjyqtqczbsl'

    msg = EmailMessage()
    msg['Subject'] = 'verify'
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = email_r
    msg.set_content(str(code_r))
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(msg)


class RejisterView(APIView):
    def post(self, request):
        # username = request.data.get('username')
        E_mail = request.data.get('email')
        password_1 = request.data.get('password_1')
        password_2 = request.data.get('password_2')
        
        if password_1 != password_2:
            return Response({'title': 'passwords did not match.'},status=status.HTTP_400_BAD_REQUEST)
        
        #validator for email
        
        try:
            o = User.objects.get(email=E_mail)
            return Response({'title': 'A user has already registered with this profile'},status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            pass

        code_rand = random.randint(100000, 999999)
        cache.set(str(E_mail), str(code_rand),3*60)
        send_mail(E_mail, code_rand)

        return Response({'title': 'The code has been emailed to you. Please enter it.'})


class create_user_view(APIView):
    def post(self, request):
        E_mail = request.data.get('email')
        code_rand = request.data.get('code')
        code_cache = cache.get(str(E_mail))
        password = request.data.get('password_1')
        if not compare_digest(code_cache, code_rand):
            return Response({'title':'The entered code is invalid'},status= status.HTTP_400_BAD_REQUEST)
        User.objects.create_user(email=E_mail, password=password)
        return Response({'title':'Your information has been successfully registered'})
        

class SeeProfoleView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        user = request.user
        profile = user.profiles
        #profile = Profile.objects.get(user=request.user)
        
        serialized = ProfileSerializer(profile, context={'request': request})
        return Response(serialized.data,status=status.HTTP_200_OK)
        


#class MyTokenObtainPairView(TokenObtainPairView):
#
#    serializer_class = MyTokenObtainPairSerializer

"""class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer"""