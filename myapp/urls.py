from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index), 
    path('login_form',views.login_form),
    path('manager_dashboard',views.manager_dashboard),
    path('team_lead_dashboard',views.team_lead_dashboard),
    path('member_dashboard',views.member_dashboard),
    path('create_project/',views.create_project, name="create_project"),

    path('display_project',views.display_project,name="display_project"),
    path('display_project_details/<int:id>',views.display_project_details,name="display_project_details"),

    path('create_project/project_submit',views.project_submit),
    
    path('update_project',views.update_project),
    path('update_project_submit/<int:id>',views.update_project_submit,name="update_project_submit"),

    path('create_task',views.create_task)
   

  
]
