from django.contrib import admin
from .models import Recipe, Category, Ingredient, RecipeIngredient
# from orderable.admin import OrderableAdmin, OrderableTabularInline
class IngredientsInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 1

class CategoriesInline(admin.TabularInline):
    model = Recipe.categories.through
    extra = 1
    classes = ['collapse']
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline,
		CategoriesInline
	]
    exclude = ["categories", "ingredients"]
    
class IngredientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)
admin.site.register(Ingredient, IngredientAdmin)