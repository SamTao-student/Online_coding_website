from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=128,null=True)
    descriptions = models.TextField(null=True)
    scripts = models.TextField(null=True)
    c_time = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=128)
