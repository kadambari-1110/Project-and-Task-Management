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
        project_object = project(name=name,description=description,deadline=date,team_lead=user.objects.get(name=team_lead))
        project_object.save()

        return redirect("display_project")


def display_project(request):
        project_object = project.objects.all()
        return render(request,"display_project.html",{"projects":project_object})


def display_project_details(request,id):
    project_object = project.objects.get(id=id)
    return render(request,"display_project_details.html",{"project":project_object})

def update_project(request):
        project_object = project.objects.all()
        return render(request,"update_project.html",{"projects":project_object})

def update_project_submit(request, id):
    try:
        project_object = project.objects.get(id=id)
    except project.DoesNotExist:
        return HttpResponse("Project not found")

    if request.method == "POST":
        # Update fields from the form
        project_object.name = request.POST.get("name")
        project_object.description = request.POST.get("description")
        team_lead = request.POST.get("team_lead")
        project_object.team_lead = user.objects.get(name=team_lead)
        project_object.deadline=request.POST.get("deadline")
        # Add other fields if your model has them

        project_object.save()
        return redirect("/display_project_details/" + str(project_object.id))  
    else:
        return render(request, "update_project_submit.html", {"project": project_object})
    

def delete(request):
    project_object = project.objects.all()
    return render(request,"delete.html",{"projects":project_object})

def delete_project(request,id):
    project_object = project.objects.get(id=id)
    project_object.delete()
    return redirect("display_project")


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


def display_task(request):
        project_object = task.objects.all()
        return render(request,"display_task.html",{"projects":project_object})


def display_task_details(request, id):
    if task.objects.filter(id=id).exists():
        task_object = task.objects.get(id=id)
        return render(request, "display_task_details.html", {"task": task_object})
    else:
        return HttpResponse("Task not found", status=404)

def update_task(request):
    task_object = task.objects.all()
    return render(request, "update_task.html", {"task": task_object})

def update_task_submit(request, id):
    if task.objects.filter(id=id).exists():
        task_object = task.objects.get(id=id)
    else:
        return HttpResponse("Task not found", status=404)

    if request.method == "POST":
        task_object.name = request.POST.get("name")
        task_object.description = request.POST.get("description")
        members = request.POST.get("member")
        deadline = request.POST.get("deadline")
        status = request.POST.get("status")

        if user.objects.filter(name=members).exists():
            task_object.team_lead = user.objects.get(name=members)
        else:
            return HttpResponse("Team lead not found", status=400)

        task_object.deadline = deadline
        task_object.status = status
        task_object.save()

        return redirect("/display_task_detail/" + str(task_object.id))  # adjust this URL as needed

    return HttpResponse("Invalid request method", status=405)
       