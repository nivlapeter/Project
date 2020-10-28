from django.shortcuts import render, redirect
from .models import Project,Profile,Ratings,Categories
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    current_user = request.user
    projects = Project.objects.order_by('pub_date').all()

    return render(request,'index.html',{"projects":projects})
