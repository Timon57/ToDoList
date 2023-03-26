from django.db import models

# Create your models here.

class Task(models.Model):
    task_name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(blank=True,null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name
