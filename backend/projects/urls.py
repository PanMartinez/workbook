from django.urls import path

from projects.views import projects_list

path('projects/list/', projects_list),
