from django.db import models

# Create your models here.
from django.contrib.auth.models import User


User._meta.get_field('username')._unique = True
User._meta.get_field('email')._unique = True


class Plan(models.Model):
    user_pk = models.ForeignKey(User,on_delete=models.CASCADE, default="")
    date = models.CharField(default="",max_length= 40)
    title = models.CharField(default="",max_length=40)
    description = models.CharField(default="", max_length=30)
    type = models.CharField(max_length=30, default="")
    time = models.CharField(max_length=30,default="")
    group_name = models.CharField(max_length=40,default="")


class Message(models.Model):
    username = models.CharField(default="",max_length=30)
    date = models.DateTimeField(auto_now=True)
    message = models.TextField(default="")
    group_name = models.CharField(max_length=40,default="")



class Group(models.Model):
    name = models.CharField(default="",max_length=40,unique=True)

