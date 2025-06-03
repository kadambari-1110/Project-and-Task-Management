from django.shortcuts import render,HttpResponse
from.models import project,task

def home(request):
    return render(request,"home.html")

def login(request):
    return render(request, "login.html")



def index(request):
    return render(request, "index.html")


def manager_dashboard(request):
    return render(request,"manager_dashboard.html")

def team_lead_dashboard(request):
    return render(request,"team_lead_dashboard.html")


def member_dashboard(request):
    return render(request,"member_dashboard.html")

def create_project(request):
  return render(request,"create_project.html")


def create_task(request):
     return render(request,"create_task.html")