from django.urls import path

from projects.views import projects_list

urlpatterns = [

    path('list/', projects_list),

]
