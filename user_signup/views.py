from django.shortcuts import render
from django.contrib.auth.models import User
from .serializers import AuthenticationSerializer
from rest_framework import generics

# Create your views here.


class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = AuthenticationSerializer
