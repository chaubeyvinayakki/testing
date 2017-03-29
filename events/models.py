from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    date_time = models.DateTimeField(auto_now_add=False,blank=True)
    duration=models.CharField(max_length=10)
    address = models.CharField(max_length=255,blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)





class userinfo(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50,blank=True)
    dob = models.DateField(max_length=10)
    gender = models.CharField(max_length=10)
    country = models.CharField(max_length=15)
    state = models.CharField(max_length=20)
    city = models.CharField(max_length=15)
    #phonenumber = models.IntegerField()


class log(models.Model):
    email= models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
