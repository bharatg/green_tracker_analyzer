from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the usertable index.")

def weekly(request):
    last_week_list = Habit.query_all()
    return HttpResponse("You're looking at the weekly view"+last_week_list)




