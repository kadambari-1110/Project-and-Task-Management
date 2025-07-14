from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index,name="index"), 
    path('login_form',views.login_form),
    path('manager_dashboard',views.manager_dashboard),
    path('team_lead_dashboard',views.team_lead_dashboard),
    path('member_dashboard',views.member_dashboard),
    path('create_project/',views.create_project, name="create_project"),

    path('display_project',views.display_project,name="display_project"),
    path('display_project_details/<int:id>',views.display_project_details,name="display_project_details"),

    path('create_project/project_submit',views.project_submit),
    
    path('update_project',views.update_project,name="update_project"),
    path('update_project_submit/<int:id>',views.update_project_submit,name="update_project_submit"),

    path('delete/',views.delete,name="delete"),
    path('delete_project/<int:id>',views.delete_project,name="delete_project"),

    path('create_task',views.create_task,name="create_task"),
    
    path('admin_session_end',views.admin_session_end,name="admin_session_end"),
    path('team_lead_session_end',views.team_lead_session_end,name="team_lead_session_end"),
    path('member_session_end',views.member_session_end,name="member_session_end"),

    path('task_submit',views.task_submit,name="task_submit"),
    path('display_task',views.display_task,name="display_task"),

    path('update_task',views.update_task,name="update_task"),
    path('delete_task',views.delete_task,name="delete_task"),
   path('view_task',views.view_task),
   path('edit_task',views.edit_task),
   

  
]
