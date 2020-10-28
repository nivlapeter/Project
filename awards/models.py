from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Project
# Profile
# Ratings
#categories

class Project(models.Model):
    title=models.CharField(max_length=30)
    Image=CloudinaryField('image',default="")
    Description=models.TextField(max_length=255)
    live_link=models.CharField(max_length=255)
    design=models.IntegerField(blank=True,default='')
    usability=models.IntegerField(blank=True,default='')
    creativity=models.IntegerField(blank=True,default='')
    content=models.IntegerField(blank=True,default='')
    overall=models.IntegerField(blank=True,default='')
    categories=models.ManyToManyField(categories)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    profilepic=CloudinaryField('image',default="")
    bio=models.TextField(max_length=255)
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)
    contact=models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Ratings(models.Model):
    design=models.IntegerField(default='')
    usability=models.IntegerField(default='')
    content=models.IntegerField(default='')
    score=models.IntegerField(default='')
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Categories(models.Model):
    categories=models.CharField(max_length=255)

    def __str__(self):
        return self.title







