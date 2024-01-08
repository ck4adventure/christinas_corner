from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator
# from orderable.models import Orderable

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
        verbose_name = "Ingredient",
        # db_comment = "Name of food ingredient",
        help_text = "Name of ingredient. Should be either 'descriptor item' or 'item, descriptor'",
        unique = True,
        max_length = 100,
        validators = [MaxLengthValidator(100)],
	)
	class Meta:
		indexes = [
            models.Index(fields=["name"])
        ]
	def __str__(self):
		return self.name

# class Step(models.Model):
#     text = models.CharField(
#         verbose_name = "Step",
#         # db_comment = "Text for a single step in a set of directions",
#         help_text = "Text for a single step within the recipe directions",
#         max_length = 400,
#         validators = []
#     )
#     # class Meta:
#     #     ordering = ["ordinal"]
#     #     # indexes = ["recipe"]
#     def __str__(self):
#         return self.text[:20]

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
	# steps = models.ManyToManyField(Step)
	def __str__(self):
		return self.name


class RecipeIngredient(models.Model):
    # this list sets the abbreviations
	PINCH = "pinch"
	TSP = "tsp"
	TBSP = "tbsp"
	CUP = "c"
	PINT = "pt"
	QUART = "qt"
	GALLON = "gal"
	OUNCE = "oz"
	LITER = "l"
	MILLILITER = "ml"
	GRAM = "g"
	KILOGRAM = "kg"
	SPACER = "none"
	
	# this maps the abbreviations above as keys to their human readable labels
	MEASURING_UNIT_CHOICES = {
		PINCH: "pinch",
		TSP: "teaspoon",
		TBSP: "tablespoon",
		CUP: "cup",
		PINT: "pint",
		QUART: "quart",
		GALLON: "gallon",
		OUNCE: "ounce",
		LITER: "liter",
		MILLILITER: "milliliter",
		GRAM: "gram",
		KILOGRAM: "kilogram",
		SPACER: " ",
	}
 
	recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
	quantity = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        help_text="Quantity is used in combination with measure and ingredient to form a recipe ingredient."
        )
	# this is not as controlled as creating a subclass, but will do for now
	measure = models.CharField(
		max_length=6,
		choices=MEASURING_UNIT_CHOICES,
		default=SPACER,
	)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
	def __str__(self):
		return f"{self.quantity} {self.measure} {self.ingredient}"

