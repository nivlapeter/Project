from django import forms
from .models import Project, Ratings,Profile

#RatingsForm
#UploadForm
#ProfilForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['profilepic','bio','contact','uname']

class UploadForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['design','usability','creativity','content','overall','pub_date','user']

class RatingsForm(forms.ModelForm):
    class Meta:
        model=Ratings
        exclude=['profile','project','score']

