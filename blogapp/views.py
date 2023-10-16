from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User

# Create your views here.

class BlogView(viewsets.ModelViewSet):
    queryset=Blog.objects.all()
    serializer_class=BlogSerializer
    permission_classes=[IsAuthenticated]
    authentication_classes=(TokenAuthentication,)


class UserView(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer

    
