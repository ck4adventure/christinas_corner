from django import forms
from django.forms import formset_factory
from .models import Recipe, Ingredient, RecipeIngredient


class IngredientForm(forms.Form):
    quantity = forms.DecimalField(
        max_digits=6,
        max_value=1000,
        min_value=0.1,
        decimal_places=2,
        required=True,
        label="Qty",
    )
    measure = forms.ChoiceField(
        choices=RecipeIngredient.MEASURING_UNIT_CHOICES, required=True, label="Measure"
    )
    ingredient = forms.ModelChoiceField(
        queryset=Ingredient.objects.all(),
        empty_label="Select an ingredient",
        required=True,
    )

IngredientFormset = formset_factory(IngredientForm, extra=2)

class AddRecipeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=2,
        strip=True,
        empty_value="Recipe Name Goes Here",
        required=True,
        label="Recipe Name",
    )
    main_ingr = forms.ChoiceField(
        choices=Recipe.MAIN_INGREDIENT_CHOICES,
        required=True,
        label="Main Ingredient",
    )
    category = forms.ChoiceField(
        choices=Recipe.CATEGORY_CHOICES, required=True, label="Category"
    )


    # can declare custom validation methods via clean_<fieldname>
    # def clean_data(self):
    #     data = self.cleaned_data
    #     return data

    # class Meta:
    #     fields = ["name"]
