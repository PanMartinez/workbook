from django.urls import path

from .views import list_users

users_urlpatterns = [
    path('users/list/', list_users),
]

