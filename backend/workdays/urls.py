from django.urls import path

from workdays.views import workdays_list

workdays_urlpatterns = [
    path('workdays/list/', workdays_list),

]
