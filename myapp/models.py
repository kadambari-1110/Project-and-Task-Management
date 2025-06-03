from django.db import models

# Create your models here.

class user(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('team_leader', 'Team Leader'),
        ('member', 'Member'),
    )
    name = models.CharField(max_length=20)
    contact_no = models.IntegerField()
    role = models.CharField(max_length=20,choices=ROLE_CHOICES,default='member')
    user_id = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    team_lead = models.ForeignKey(user,related_name="teamleader",on_delete=models.CASCADE)
    deadline = models.DateField()

    def __str__(self):
        return self.name
    

class task(models.Model):
    project = models.ForeignKey(project,on_delete=models.CASCADE,related_name="tasks")
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)  
    members = models.ForeignKey(user,on_delete=models.CASCADE,related_name="member")
    status = models.CharField(choices=[('Pending','Pending'),('Completed','Completed')],max_length=100)
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name