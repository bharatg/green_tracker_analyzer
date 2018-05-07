from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from usertable.serializers import UserSerializer

def index(request):
    return HttpResponse("Hello, world. You're at the usertable index.")

# API endpoint for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

def weekly(request):
    last_week_list = Habit.query_all()
    return HttpResponse("You're looking at the weekly view"+last_week_list)




