from django.shortcuts import render, get_object_or_404
from .models import Recipe
# Create your views here.
# beef, chicken
def index(request):
    recipe_list = Recipe.objects.all()
    keys = Recipe.MAIN_FOCUS_CHOICES.keys()
    cat_dict = {}
    for key in keys:
        item = recipe_list.filter(main_focus=key)
        cat_dict[key] = item
    context = {"recipe_list": recipe_list, "recipe_dict": cat_dict }
    return render(request, "recipes/index.html", context)

def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})
