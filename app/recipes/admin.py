from django.contrib import admin
from .models import Recipe, Category
# Register your models here.

class CategoriesInline(admin.TabularInline):
    model = Recipe.categories.through
    extra = 1
    
class RecipeAdmin(admin.ModelAdmin):
    inlines = [
		CategoriesInline
	]
    exclude = ["categories"]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category)