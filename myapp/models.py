from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    team_lead = models.ForeignKey(User,related_name="teamleader",on_delete=models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.name
    

class task(models.Model):
    project = models.ForeignKey(project,on_delete=models.CASCADE,related_name="tasks")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)  
    members = models.ForeignKey(User,on_delete=models.CASCADE,related_name="member")
    status = models.CharField(choices=[('Pending','Pending'),('Completed','Completed')])
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name