from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):

    name = models.CharField(max_length=50,null=True)
    status = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
