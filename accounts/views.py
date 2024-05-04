from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserRegisterSerializers
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.

class UserRegister(APIView):
    def post(self,request):
        ser_data = UserRegisterSerializers(data=request.POST)
        if ser_data.is_valid():
            ser_data.create(ser_data.validated_data)
            # User.objects.create_user(
            #     username=ser_data.validated_data['username'],
            #     email = ser_data.validated_data['email'],
            #     password = ser_data.validated_data['password'],
            # )
            return Response(ser_data.data,status=status.HTTP_201_CREATED)
        return Response(ser_data.errors,status=status.HTTP_400_BAD_REQUEST)
