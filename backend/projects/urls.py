from django.urls import path

from projects.views import projects_list

projects_urlpatterns = [
    path('projects/list/', projects_list),
]
