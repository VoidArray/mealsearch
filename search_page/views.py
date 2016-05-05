from django.http import HttpResponse
from django.shortcuts import render

from .models import Ingredient, Recipe, AlterIngredient, ListIngredient


def index(request):
    return HttpResponse("Hello, world!")

def search_result(request, search):
    ingerdient_list = Ingredient.objects.all()
    output = ', '.join([i.name for i in ingerdient_list])
    return HttpResponse(output + '\n' + search)