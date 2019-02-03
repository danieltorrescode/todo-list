from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    STATUS_ID = (
        (0, 'To-do'),
        (1, 'In-progress'),
        (2, 'Done'),
    )
    name = models.CharField(max_length=50,null=True)
    status = models.IntegerField(default=0, choices=STATUS_ID)

    @property
    def get_status(self):
        if self.status is 0:
            return 'To-do'
        elif self.status is 1:
            return 'In-progress'
        else:
            return 'Done'