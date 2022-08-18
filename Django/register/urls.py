from django.shortcuts import render


from django.urls import path
from register.views import RegisterList, LoginAPIView


app_name = 'register'

urlpatterns = [
    path('register/', RegisterList.as_view(),name='register'),
    path('login/', LoginAPIView.as_view(), name='login')
    
]