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
    path('create_project/project_submit',views.project_submit),
    path('create_task',views.create_task)
   

  
]
