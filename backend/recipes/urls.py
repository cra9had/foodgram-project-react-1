from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

app_name = "api_recipes"

api_recipes_router = DefaultRouter()
api_recipes_router.register("tags", TagViewSet)
api_recipes_router.register("ingredients", IngredientViewSet)
api_recipes_router.register("recipes", RecipeViewSet)

urlpatterns = [
    path("", include(api_recipes_router.urls)),
]
