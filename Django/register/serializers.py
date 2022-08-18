from rest_framework import serializers
from .models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed



class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=60,
                                     min_length=8, write_only=True)
                                     

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should contain alphanumeric characters')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

 

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=200,min_length=3)
    password = serializers.CharField(max_length=68, min_length=10, write_only=True)
    username = serializers.CharField(max_length=68, min_length=10, read_only=True)
   
    
    class Meta:
        model = User
        fields = ['email', 'password','username']
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        user = auth.authenticate(email=email, password=password)
        
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
       
        
        
        return{
            'email':user.email,
            'username': user.username,
         
        }
        return super().validate(attrs)
   
     
        
    