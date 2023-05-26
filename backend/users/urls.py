from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

app_name = "api_users"

api_users_router = DefaultRouter()
api_users_router.register("users", CustomUserViewSet)

urlpatterns = [
    path("", include(api_users_router.urls)),
    path("auth/", include("djoser.urls.authtoken")),
]
