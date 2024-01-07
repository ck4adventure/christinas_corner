from django.urls import path
from . import views

app_name = "recipes"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:recipe_id>/", views.detail, name="detail"),
    path("main-ingredient/<str:ingr>/", views.main_ingredient_detail, name="main_ingredient"),
    path("category/<str:category>/", views.category_detail, name="category"),
]