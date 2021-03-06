from django.db import models

# Import User model. 
from users.models import User

# Create your models here.

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=60)
    

class Category(models.Model):
    category_name = models.CharField(max_length=60)

class Drink(models.Model):
    drink_name = models.CharField(max_length=60)
    drink_instructions = models.CharField(max_length=60)
    drink_image = models.URLField(blank=True, default="https://www.salonlfc.com/wp-content/uploads/2018/01/image-not-found-scaled-1150x647.png")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="cocktail_category")
    favorites = models.ManyToManyField(User, related_name="drink_in_favorite", blank=True)
    ingredients = models.ManyToManyField(Ingredient, related_name="drink_ingredients", blank=True)
