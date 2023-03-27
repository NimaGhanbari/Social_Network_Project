from django.shortcuts import render
from django.conf import settings
from rest_framework.views import APIView
from django.contrib.auth import get_user_model 
from rest_framework.response import Response
import random
from django.core.cache import cache
import mailtrap as mt
import smtplib
from email.message import EmailMessage
from rest_framework import status
User = get_user_model()

def send_mail(email_r, code_r):
    # اگر از گوگل برای ارسال ایمیل هامون استفاده میکنیم مقدار هاستش به شکل زیر است
    EMAIL_HOST = 'smtp.gmail.com'
    # اگر از  فرستنده خارجی استفاده کردیم هاستش را به ما میدهند
    # ایمیلی که براش اپ پسورد زدیم که فرستتنده ایمیل است را مینویسیم


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
            #user = User.objects.create(email=E_mail, password=password)
            pass

        code_rand = random.randint(100000, 999999)
        cache.set(str('email'), code_rand, 3*60)
        send_mail(E_mail, code_rand)
        return Response({'title': 'The code has been emailed to you. Please enter it.'})


class create_user_view(APIView):
    def post(self, request):
        E_mail = request.data.get('email')
        code_rand = request.data.get('code')
        code_cache = cache.get(str(E_mail))
        password = request.data.get('password_1')
        if code_cache != code_cache:
            return Response({'title':'The entered code is invalid'},status= status.HTTP_400_BAD_REQUEST)
        User.objects.create(email=E_mail, password=password)
        return Response({'title':'Your information has been successfully registered'})
        
