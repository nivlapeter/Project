from django.shortcuts import render, redirect
from .models import Project,Profile,Ratings,Categories
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email

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

@login_required(login_url='/accounts/login/')
def project(request, project_id):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    message=f'{"Gratitude for your participation"}'
    project = Project.objects.filter(project_id=id)
    ratings = Ratings.objects.filter(project=project)
    design = ratings.aggregate(Avg('design'))['design__avg']
    usability = ratings.aggregate(Avg('usability'))['usability__avg']
    creativity = ratings.aggregate(Avg('creativity'))['creativity__avg']
    content = ratings.aggregate(Avg('content'))['content__avg']
    score = ratings.aggregate(Avg('score'))['score__avg']

    if request.method == 'POST':
        form = RatingsForm(request.POST)
        if form.is_valid():
            ratings = form.save(commit=False)
            ratings.score = (ratings.design + ratings.usability + ratings.creativity + ratings.content) / 3
            ratings.project = project
            ratings.user = user
            ratings.save
        return redirect('project', project_id)
    else:
        form = RatingsForm()
        return render(request,'project.html',{"project":project,"ratings":ratings,"form":form,"design":design,"usability":usability,"creativity":creativity,"content":content,"score":score} )

@login_required(login_url='/accounts/login/')
def upload_project(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()
        # take a look later(email)
        # if form.is_valid(): 
        #     name = form.cleaned_data['your_name']
        #     email = form.cleaned_data['email']
        #     recipient = UploadFormRecipients(name = name,email =email)
        #     recipient.save()
        #     send_welcome_email(name,email)        
        return redirect('index')
    else:
        form = UploadForm()
        return render(request, 'upload_project.html',{"form":form,"profile":profile})

@login_required(login_url='/accounts/login/')
def search(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if 'project' in request.GET and request.GET["project"]:
        search_term=request.GET.get("project")
        searched_project=project.search_project(search_term)
        message=f"{search_term}"

        return render(request,'search.html',{"message":message,"project":searched_project,"profile":profile})
    else:
        message="sorry! you haven't searched for any item"
        return render(request,'/search.html',{"message":message,"project":searched_project,"profile":profile})

