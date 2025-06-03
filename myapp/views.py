from django.shortcuts import render,HttpResponse,redirect
from.models import project,task,user


def index(request):
    return render(request, "index.html")

def login_form(request):
    if request.method == "POST":
        us = request.POST['username']
        ps = request.POST['password']
        user_object = user.objects.get(user_id=us,password=ps)
        if user_object:
            role = user_object.role
            if role == "admin":
                return redirect('/manager_dashboard')
            elif role == "team_leader":
                return redirect('/team_lead_dashboard')  
            elif role == "member":
                return redirect('/member_dashboard')
            else:
                return HttpResponse("Error")
        else:
            return HttpResponse("Incorrect Credentials")
        

def project_submit(request):
    if request.method == "POST":
        name = request.POST['name']
        description = request.POST['description']
        date = request.POST['deadline']
        team_lead = request.POST['team_lead']
        proj = project(name=name,description=description,deadline=date,team_lead=user.objects.get(id=team_lead))
        proj.save()

        return HttpResponse("Project Created")

def manager_dashboard(request):
    return render(request,"manager_dashboard.html")

def team_lead_dashboard(request):
    return render(request,"team_lead_dashboard.html")


def member_dashboard(request):
    return render(request,"member_dashboard.html")

def create_project(request):
    users = user.objects.filter(role="team_leader")
    return render(request,"create_project.html",{'users':users})


def create_task(request):
     return render(request,"create_task.html")