from django.db import models
from datetime import datetime

# Create your models here.
class Employee(models.Model):
    username=models.CharField(max_length=50,default="")
    firstname=models.CharField(max_length=50,default="")
    lastname=models.CharField(max_length=50,default="")
    email=models.CharField(max_length=50,default="")
    created=models.DateTimeField(blank=True,default=datetime.now())

    def __str__(self):
        return self.username
    