from django.shortcuts import render, get_object_or_404
from .models import Recipe


# Create your views here.
# beef, chicken
def index(request):
    recipe_list = Recipe.objects.all()
    context = {"recipe_list": recipe_list, "categories": Recipe.MAIN_INGREDIENT_CHOICES}
    return render(request, "recipes/index.html", context)

def main_ingredient_detail(request, ingr):
    # todo validate cat
    print(ingr)
    recipe_list = Recipe.objects.filter(main_ingredient=ingr)
    context = {
        "recipe_list": recipe_list,
        "main_ingredient": Recipe.MAIN_INGREDIENT_CHOICES[ingr],
    }
    return render(request, "recipes/main_ingredient_detail.html", context)

def category_detail(request, cat):
    print(cat)
    recipe_list = Recipe.objects.filter(category=cat)
    context = {
		"recipe_list":recipe_list,
		"category": cat
	}
    return render(request, "recipes/category_detail.html", context)


def detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    return render(request, "recipes/detail.html", {"recipe": recipe})
