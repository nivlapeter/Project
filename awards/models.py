from django.db import models
from cloudinary.models import CloudinaryField
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
# Project
# Profile
# Ratings
#categories

class Categories(models.Model):
    title=models.CharField(max_length=255)

    def __str__(self):
        return self.title


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
    categories=models.ManyToManyField(Categories)
    pub_date=models.DateTimeField(default=timezone.now)
    user=models.OneToOneField(User,on_delete=models.CASCADE, default="")

    def __str__(self):
        return self.title

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE, default="")
    uname=models.CharField(max_length=100)
    profilepic=CloudinaryField('image',default="")
    bio=models.TextField(max_length=255)
    projects=models.ForeignKey(Project,on_delete=models.CASCADE)
    contact=models.CharField(max_length=30)

    def __str__(self):
        return f'{self.uname} Profile'

    
    @classmethod
    def search_project(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

class Ratings(models.Model):
    design=models.IntegerField(default='')
    usability=models.IntegerField(default='')
    content=models.IntegerField(default='')
    creativity=models.IntegerField(default='')
    score=models.IntegerField(default='')
    project=models.ForeignKey(Project, on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile, on_delete=models.CASCADE)

   









