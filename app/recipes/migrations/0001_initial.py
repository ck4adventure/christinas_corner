# Generated by Django 5.0 on 2024-01-09 06:12

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_ingredient', models.CharField(choices=[('BEEF', 'Beef'), ('CHICKEN', 'Chicken'), ('PORK', 'Pork'), ('EGGS', 'Eggs'), ('VEGETABLE', 'Vegetable'), ('DAIRY', 'Dairy'), ('GRAINS', 'Grain'), ('LEGUMES', 'Legumes'), ('SUGAR', 'Sugar')], default='VEGETABLE', max_length=9)),
                ('category', models.CharField(choices=[('BREAD', 'Bread'), ('BREAKFAST', 'Breakfast'), ('CAKE', 'Cakes'), ('COOKIES', 'Cookies'), ('CURRIES', 'Curries'), ('FERMENTS', 'Ferments'), ('MAIN', 'Main'), ('NOODLES', 'Noodles'), ('PASTRY', 'Pastry'), ('PIES', 'Pies'), ('RICE', 'Rice'), ('SIDE', 'Side'), ('SALAD', 'Salad'), ('SPICE', 'Spice Blend'), ('TARTS', 'Tarts')], default='BREAD', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Name of ingredient. Should be either 'descriptor item' or 'item, descriptor'", max_length=100, unique=True, validators=[django.core.validators.MaxLengthValidator(100)], verbose_name='Ingredient')),
            ],
            options={
                'indexes': [models.Index(fields=['name'], name='recipes_ing_name_164c6a_idx')],
            },
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=2, help_text='Quantity is used in combination with measure and ingredient to form a recipe ingredient.', max_digits=6)),
                ('measure', models.CharField(choices=[('pinch', 'pinch'), ('tsp', 'teaspoon'), ('tbsp', 'tablespoon'), ('c', 'cup'), ('pt', 'pint'), ('qt', 'quart'), ('gal', 'gallon'), ('oz', 'ounce'), ('l', 'liter'), ('ml', 'milliliter'), ('g', 'gram'), ('kg', 'kilogram'), ('none', ' ')], default='none', max_length=6)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.recipe')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, db_index=True)),
                ('text', models.CharField(help_text='Text for a single step within the recipe directions', max_length=400, verbose_name='Step')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='recipes.recipe')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]
