# Generated by Django 3.1.2 on 2020-11-02 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0008_project_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
    ]
