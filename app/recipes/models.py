from django.db import models


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
	MAIN_FOCUS_CHOICES = {
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
	main_focus = models.CharField(
        max_length=9,
		choices=MAIN_FOCUS_CHOICES,
  		default=VEGETABLE
	)

	def __str__(self):
		return self.name
