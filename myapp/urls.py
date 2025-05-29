from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home), 
    path('index',views.index),
    path('login',views.login),
    path('manager_dashboard',views.manager_dashboard),
    path('team_lead_dashboard',views.team_lead_dashboard),
    path('member_dashboard',views.member_dashboard),

  
]