from django.db import models
from django.contrib.auth.models import User
from rest_framework import permissions, authentication



# Create your models here


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
