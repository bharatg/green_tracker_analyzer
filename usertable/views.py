from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from usertable.serializers import UserSerializer, HabitSerializer

from usertable.models import User as Usr
from usertable.models import Habit as Hab

def index(request):
    return HttpResponse("Hello, world. You're at the usertable index.")

# API endpoint for User
class UserViewSet(viewsets.ModelViewSet):
    queryset = Usr.objects.all().order_by('uid')
    serializer_class = UserSerializer

@csrf_exempt
def user_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        users = Usr.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def user_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        user = Usr.objects.get(pk=pk)
    except Usr.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSerializer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)
    
class HabitViewSet(viewsets.ModelViewSet):
    queryset = Hab.objects.all()
    serializer_class = HabitSerializer

@csrf_exempt
def habit_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        habits = Hab.objects.all()
        serializer = HabitSerializer(habits, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = HabitSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def habit_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        habit = Hab.objects.get(pk=pk)
    except Hab.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = HabitSerializer(habit)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = HabitSerializer(habit, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        habit.delete()
        return HttpResponse(status=204)

def weekly(request):
    last_week_list = Habit.query_all()
    return HttpResponse("You're looking at the weekly view"+last_week_list)
