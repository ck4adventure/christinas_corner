from django.db import models
from orderable.models import Orderable

class Category(models.Model):
    name = models.CharField(
		max_length=20,
		unique=True,
		help_text="Name of food category, must be unique."
	)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "categories"
        
class Ingredient(models.Model):
	name = models.CharField(
		max_length=100,
	)
	def __str__(self):
		return self.name

# Create your models here.
class Recipe(models.Model):
	BEEF = "BEEF"
	CHICKEN = "CHICKEN"
	PORK = "PORK"
	EGGS = "EGGS"
	VEGETABLE = "VEGETABLE"
	DAIRY = "DAIRY"
	GRAINS = "GRAINS"
	LEGUMES = "LEGUMES"
	SUGAR = "SUGAR"
	MAIN_INGREDIENT_CHOICES = {
        BEEF: "Beef",
        CHICKEN: "Chicken",
        PORK: "Pork",
        EGGS: "Eggs",
        VEGETABLE: "Vegetable",
        DAIRY: "Dairy",
        GRAINS: "Grains",
        LEGUMES: "Legumes",
        SUGAR: "Sugary Sweet"
    }
	
	name = models.CharField(max_length=100)
	main_ingredient = models.CharField(
        max_length=9,
		choices=MAIN_INGREDIENT_CHOICES,
  		default=VEGETABLE
	)
	categories = models.ManyToManyField(Category)

	def __str__(self):
		return self.name


class RecipeIngredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
	quantity = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Quantity is used in combination with measure and ingredient to form a recipe ingredient."
        )
	measure = models.CharField(
		max_length=9,
	)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
	def __str__(self):
		return f"{self.quantity} {self.measure} {self.ingredient}"
