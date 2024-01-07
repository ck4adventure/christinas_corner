# Generated by Django 5.0 on 2024-01-07 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of food category, must be unique.', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('main_ingredient', models.CharField(choices=[('BEEF', 'Beef'), ('CHICKEN', 'Chicken'), ('PORK', 'Pork'), ('EGGS', 'Eggs'), ('VEGETABLE', 'Vegetable'), ('DAIRY', 'Dairy'), ('GRAINS', 'Grains'), ('LEGUMES', 'Legumes'), ('SUGAR', 'Sugary Sweet')], default='VEGETABLE', max_length=9)),
                ('categories', models.ManyToManyField(to='recipes.category')),
            ],
        ),
    ]
