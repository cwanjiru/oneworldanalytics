from django.shortcuts import render
from rest_framework import generics,status
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.response import Response

from django.conf import settings
from .models import User

class RegisterList(generics.ListCreateAPIView): 
    queryset = User.objects.all() 
    serializer_class = RegisterSerializer 
    name = 'register' 

class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)



