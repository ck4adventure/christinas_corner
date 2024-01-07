from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MaxLengthValidator

# Quantity Field needs to be invoked with its base unit like 'gram' or 'cup'
# then when a new object is added it can give the amount
from quantityfield.fields import QuantityField


class Ingredient(models.Model):
    name = models.CharField(
        verbose_name = "Ingredient",
        db_comment = "Name of food ingredient",
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

    
class Step(models.Model):
    text = models.CharField(
        verbose_name = "Step",
        # db_comment = "Text for a single step in a set of directions",
        help_text = "Text for a single step within the recipe directions",
        max_length = 400,
        validators = []
    )
    # class Meta:
    #     ordering = ["ordinal"]
    #     # indexes = ["recipe"]
    def __str__(self):
        return self.text[:20]


class Recipe(models.Model):
    name = models.CharField(
        max_length = 200,
        # db_comment = "Name of Recipe",
        help_text = "Name of Recipe. Should not include authors name unless explicitly so titled.",
        # choosing unique false here, will eventually do a more complex comparison validation
        unique = False,
        validators = [],
    )
    ingredients = models.ManyToManyField(
        Ingredient, 
        through = "RecipeIngredients",
        through_fields = ("recipe","ingredient")
	)
    # steps = models.ManyToManyField(Step)
    # ingredients = models.ManyToManyField(Ingredient,through="RecipeIngredients", through_fields=("recipe", "ingredient"))
    class Meta:
        indexes = [
            models.Index(fields=["name"]),
        ]
    def __str__(self):
        return self.name


# Although Dj has a ManyToManyField which will auto-create a joins, here I want finer control
class RecipeIngredients(models.Model):
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
	}

	recipe = models.ForeignKey(Recipe, on_delete=models.RESTRICT)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
	quantity = models.DecimalField(
        max_digits=5, 
        decimal_places=2
    )
	# this is not as controlled as creating a subclass, but will do for now
	measure = models.CharField(
		max_length=5,
		choices=MEASURING_UNIT_CHOICES,
		default=CUP,
	)
	
	class Meta:
		indexes = ["recipe", "ingredient"]
		constraints = [
			models.UniqueConstraint(
				fields = ['recipe', 'ingredient'],
				name = "unique_recipe_ingredient_keypairs")
		]
    
	def __str__(self):
		return f"{self.recipe.name} {self.ingredient.name}"
 	
	def is_imperial(self):
		return self.measuring_unit in {
			self.CUP,
			self.PINT,
			self.QUART,
			self.GALLON,
			self.OUNCE,
		}