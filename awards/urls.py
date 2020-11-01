"""accolades URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url('', views.index, name = 'index'),
    url('profile/(?P<username>\w{0,50})/', views.profile, name = 'myprofile'),
    url('profile/edit/', views.edit_profile, name = 'edit'),
    url('upload/', views.project_upload, name = 'upload'),
    url('project/(\d+)',views.project,name = 'project'),
    url('search/', views.search, name='search'),

    # url(r'^$', views.index, name='index'),
    # url(r'^project/(\d+)$', views.project, name='project'),
    # url(r'^upload/$', views.upload_site, name='upload'),
    # url(r'^profile/(?P<username>\w{0,50})/$', views.profile, name='profile'),
    # url(r'^update_profile/(\d+)$', views.update_profile, name='update_profile'),
    # url(r'^search/$', views.search, name='search_results'),
    # url(r'^api/profiles/$', views.ProfileList.as_view()),
    # url(r'^api/projects/$', views.ProjectList.as_view())

    # path('',views.home, name='Welcome'),
    # re_path('authorprofile/(\d+)', views.view_user, name='view_userprofile'),
    # path('new/project', views.new_project, name='new_project'),
    # re_path('viewproject/(\d+)', views.view_project, name='view_project'),
    # path('accounts/profile/', views.profile, name='user_profile'),
    # re_path('search/', views.search_results, name='search_results'),
    # path('api/projects/', views.ProjectList.as_view()),
    # path('api/profiles/', views.ProfileList.as_view()),   

]