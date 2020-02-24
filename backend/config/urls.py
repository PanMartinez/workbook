from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from projects.urls import urlpatterns as projects_urls
from users.urls import urlpatterns as users_urls
from workdays.urls import urlpatterns as workdays_urls

custom_urls = [

    # --- Django admin urls ---
    path('admin/', admin.site.urls),

    # --- JWT urls ---
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

api_urls = [

    path('projects/', include(projects_urls)),
    path('users/', include(users_urls)),
    path('workdays/', include(workdays_urls)),

]

urlpatterns = [

    path(r'api/', include(api_urls)),
    path('', include(custom_urls)),

]
