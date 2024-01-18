from django import forms


class AddRecipeForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        min_length=2,
        strip=True,
        empty_value="Recipe Name Goes Here",
        required=True,
        label="Recipe Name",
    )

    def clean_recipe_name(self):
        data = self.cleaned_data
        return data
    
    class Meta:
        fields= ["name"]
