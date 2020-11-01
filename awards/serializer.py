from rest_framework import serializers
from .models import Profile,Project


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('uname', 'bio', 'profilepic','projects','contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('title','Image','Description','link','categories','pub_date')