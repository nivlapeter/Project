from django.shortcuts import render, redirect
from .models import Project,Profile,Ratings,Categories
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .emails import send_welcome_email
from .forms import SignupForm,ProfileForm, UploadForm, RatingsForm
from django.contrib.auth import login
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectSerializer

# Create your views here.


def index(request):
    current_user = request.user
    projects = Project.objects.order_by('pub_date').all()

    return render(request,'index.html',{"projects":projects})

def registration(request):
    if request.user.is_authenticated():
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                return redirect('index')
                current_user = request.user
                name = form.cleaned_data['your_name']
                email = form.cleaned_data['email']
                recipient = UploadFormRecipients(name = name,email =email)
                recipient.save()
                send_welcome_email(name,email) 
        else:
            form = SignupForm()
        return render(request, 'registration/registration_form.html', {'form': form})

#@unauthenticated_user
def SignIn(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            form = SignupForm()
    return render(request, 'registration/login.html', {'form':form})

# def profile(request, username):
#     user = User.objects.get(username = username)
#     profile = Profile.objects.get(user = user)
#     projects = Project.objects.filter(user = user)
#     return render(request, 'profile.html', {'profile': profile, 'projects': projects})

@login_required(login_url='/accounts/login/')
def profile(request, pk_test):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    projects = Project.objects.filter(user=current_user)
    my_profile = Profile.objects.get(user=current_user)
    return render(request, 'profile.html', locals())

# @login_required(login_url = '/accounts/login/')
# def edit_profile(request, id):
#     if request.method == 'POST':
#         profile = Profile.objects.get(id = id)
#         form = ProfileForm(request.POST or None, request.FILES or None, instance = profile)
#         if form.is_valid():
#             edit = form.save(commit=False)
#             edit.save()
#             return redirect('profile', username = request.user)
#     else:
#         form = ProfileForm()

#     return render(request, 'edit_profile.html', {'form': form, "profile":profile})

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
    return render(request, 'edit_profile.html', {"form":form,"profile":profile})

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

# @login_required(login_url='/accounts/login/')
# def project_upload(request):
#     if request.method == 'POST':
#         form = UploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             project = form.save(commit=False)
#             project.user = request.user
#             project.save()
#         return redirect('index')
#     else:
#         form = UploadForm()

#     return render(request, 'upload_project.html', {'form': form, "profile":profile})

@login_required(login_url='/accounts/login/')
def project_upload(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()      
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

################################################################################


class ProfileList(APIView):
    def get(self, request, format=None):
        all_profilez = Profile.objects.all()
        serializers = ProfileSerializer(all_profilez, many=True)
        return Response(serializers.data)



class ProjectList(APIView):
    def get(self, request, format=None):
        all_projectz = Project.objects.all()
        serializers = ProjectSerializer(all_projectz, many=True)
        return Response(serializers.data)