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

@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    projects = Project.objects.filter(user=current_user)
    my_profile= = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = current_user
            edit.save()
        return redirect('myprofile')
    else:
        form=ProfileForm()
    return render(request, 'edit_profile.html', {"form":form,"profile",profile})
