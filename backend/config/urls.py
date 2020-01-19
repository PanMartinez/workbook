from django.contrib import admin
from django.urls import path

from rest_framework_simplejwt import views as jwt_views

from projects.urls import projects_urlpatterns
from users.urls import users_urlpatterns
from workdays.urls import workdays_urlpatterns

urlpatterns = [

    # --- JWT urls ---
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # --- Django admin url ---
    path('admin/', admin.site.urls),

] + projects_urlpatterns + users_urlpatterns + workdays_urlpatterns
