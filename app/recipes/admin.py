from django.contrib import admin
from .models import Recipe, Ingredient, RecipeIngredient, Step
from orderable.admin import OrderableAdmin, OrderableTabularInline

class StepsInline(OrderableTabularInline):
    model = Step
    extra = 1

class IngredientsInline(admin.StackedInline):
	model = RecipeIngredient
	extra = 1
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
        IngredientsInline,
        StepsInline,
	]
    exclude = ["ingredients"]
    
class IngredientAdmin(admin.ModelAdmin):
    pass

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)