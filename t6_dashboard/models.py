from django.db import models

class topUsers(models.Model):
    fullname = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    division = models.CharField(max_length=255)
    point = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)