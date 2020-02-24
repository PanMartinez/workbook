from django.urls import path

from workdays.views import workdays_list

urlpatterns = [

    path('list/', workdays_list),

]
