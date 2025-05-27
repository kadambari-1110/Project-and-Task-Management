from django.db import models

# Create your models here.

class project(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    # team_lead = models.ForeignKey()
    deadline = models.DateField()

    def __str__(self):
        return self.name
    

class task(models.Model):
    project = models.ForeignKey(project,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    # members = models.CharField()
    status = models.BooleanField(choices=[('Pending','Pending'),('Completed','Completed')])
    deadline = models.DateTimeField()

    def __str__(self):
        return self.name