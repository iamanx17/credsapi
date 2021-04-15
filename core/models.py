from django.db import models
from django.utils import timezone

# Create your models here.

class creds(models.Model):
    #django creds
    project_name=models.CharField(max_length=250,unique=True)
    secret_key=models.CharField(max_length=250,unique=True)
    #database creds
    database_host=models.CharField(max_length=250)
    database_user=models.CharField(max_length=250)
    database_password=models.CharField(max_length=250)
    database_name=models.CharField(max_length=250,unique=True)
    #time
    date=models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_on=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.project_name
