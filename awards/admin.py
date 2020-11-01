from django.contrib import admin
from .models import Project,Profile,Ratings,Categories

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal = ('categories')

admin.site.register(Project)
admin.site.register(Profile)
admin.site.register(Ratings)
admin.site.register(Categories)

