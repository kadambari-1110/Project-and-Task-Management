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
                request.session['admin']=us
                return redirect('/manager_dashboard')
            elif role == "team_leader":
                request.session['team_lead']=us
                return redirect('/team_lead_dashboard')  
            elif role == "member":
                request.session['member']=us
                return redirect('/member_dashboard')
            else:
                return HttpResponse("Error")
        else:
            return HttpResponse("Incorrect Credentials")
        

def project_submit(request):
    if request.session.get('admin') is not None:
        if request.method == "POST":
            name = request.POST['name']
            description = request.POST['description']
            date = request.POST['deadline']
            team_lead = request.POST['team_lead']
            project_object = project(name=name,description=description,deadline=date,team_lead=user.objects.get(name=team_lead))
            project_object.save()

            return redirect("display_project")


def display_project(request):
    if request.session.get('admin'):
        project_object = project.objects.all()
        return render(request,"display_project.html",{"projects":project_object})


def display_project_details(request,id):
    if request.session.get('admin'):
        project_object = project.objects.get(id=id)
        return render(request,"display_project_details.html",{"project":project_object})

def update_project(request):
    if request.session.get('admin'):
        project_object = project.objects.all()
        return render(request,"update_project.html",{"projects":project_object})

def update_project_submit(request, id):
    if request.session.get('admin'):
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
    if request.session.get('admin'):
        project_object = project.objects.all()
        return render(request,"delete.html",{"projects":project_object})

def delete_project(request,id):
    if request.session.get('admin'):
        project_object = project.objects.get(id=id)
        project_object.delete()
        return redirect("display_project")


def manager_dashboard(request):
    if request.session.get('admin'):
        return render(request,"manager_dashboard.html")

def team_lead_dashboard(request):
    if request.session.get('team_lead'):
        return render(request,"team_lead_dashboard.html")


def member_dashboard(request):
    if request.session.get('member'):
        return render(request,"member_dashboard.html")

def create_project(request):
    if request.session.get('admin'):
        users = user.objects.filter(role="team_leader")
        return render(request,"create_project.html",{'users':users})


def create_task(request):
     if request.session.get('team_lead'):
        temp = user.objects.get(user_id=request.session.get('team_lead'))
        id = temp.id
        project_object=project.objects.filter(team_lead=id)
        member_object=user.objects.filter(role="member")
        return render(request,"create_task.html",{"project":project_object,"members":member_object})
     

def admin_session_end(request):
    del request.session['admin']
    return redirect("index")

def team_lead_session_end(request):
    del request.session['team_lead'];
    return redirect("index")

def task_submit(request):
    if request.session.get('team_lead'):
        if request.method == "POST":
            proj = request.POST['project']
            task_name = request.POST['name']
            task_description = request.POST['description']
            members = request.POST['members']
            status = request.POST['status']
            deadline = request.POST['deadline']

            project_id = project.objects.get(id=proj)
            user_id = user.objects.get(id=members)

            task_object = task(project=project_id,name=task_name,description=task_description,members=user_id,status=status,deadline=deadline)
            task_object.save()
            
            return HttpResponse("Task Created")

def display_task(request):
    if request.session.get("team_lead"):
        team_lead_us = request.session.get("team_lead")
        user_object = user.objects.get(user_id=team_lead_us)
        team_lead_id = user_object.id
        project_object = project.objects.get(team_lead=team_lead_id)
        project_id = project_object.id
        task_object = task.objects.filter(project=project_id)
        return render(request,"display_task.html",{"tasks":task_object})
    
def update_task(request):
    if request.session.get("team_lead"):
        team_lead = request.session.get("team_lead")
        user_object = user.objects.get(user_id=team_lead)
        team_lead_id = user_object.id
        project_object = project.objects.get(team_lead=team_lead_id)
        project_id = project_object.id
        task_object = task.objects.filter(project=project_id)
        return render(request,"update_task.html",{"task":task_object})
    

def delete_task(request):
    if request.session.get("team_lead"):
        team_lead = request.session.get("team_lead")
        user_object = user.objects.get(user_id=team_lead)
        team_lead_id = user_object.id
        project_object = project.objects.get(team_lead=team_lead_id)
        project_id = project_object.id
        task_object = task.objects.filter(project=project_id)
        return render(request,"delete_task.html",{"task":task_object})

def view_task(request):
    if request.session.get("member"):
        member = request.session.get("member")
        user_object = user.objects.get(user_id=member)
        member_id = user_object.id
        task_object = task.objects.filter(members=member_id)
        return render(request,"view_task.html",{"task":task_object})


def edit_task(request):
    if request.session.get('member'):
        member = request.session.get("member")
        user_object = user.objects.get(user_id=member)
        member_id = user_object.id
        task_object = task.objects.filter(members=member_id)
        return render(request,"edit_task.html",{"task":task_object})


def member_session_end(request):
    if request.session.get('member'):
        del request.session['member']
        return redirect('index')