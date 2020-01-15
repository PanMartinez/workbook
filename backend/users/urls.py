from django.urls import path

from .views import list_users

path('users/list/', list_users),
