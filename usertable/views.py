from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from usertable.serializers import UserSerializer, HabitSerializer

from usertable.models import User as Usr
from usertable.models import Habit as Hab

def index(request):
    return HttpResponse("Hello, world. You're at the usertable index.")

# API endpoint for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usr.objects.all().order_by('uid')
    serializer_class = UserSerializer

class HabitViewSet(viewsets.ModelViewSet):
    queryset = Hab.objects.all()
    serializer_class = HabitSerializer

def weekly(request):
    last_week_list = Habit.query_all()
    return HttpResponse("You're looking at the weekly view"+last_week_list)
