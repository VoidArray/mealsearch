from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=300)

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

class AlterIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, related_name='id_ingredient')
    alternative = models.ForeignKey(Ingredient, related_name='id_complimentary_ingredient')

class ListIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='id_recipe')
    alteringredient = models.ForeignKey(AlterIngredient, related_name='id_ingridient_w_alter')

