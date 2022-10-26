from django.http import Http404, HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.recipes.factory import make_recipe

from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(
        is_published=True,
    ).order_by('-id')
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id,
        is_published=True,
    ).order_by('-id')

    #category_name = getattr(recipes.first(), 'category', None),

    if not recipes:
        return HttpResponse(content='Not found :(', status=404)
        raise Http404('mensagem')

    # recipes = get_list_or_404(
    #    Recipe.objects.filter(
    #        category__id=category_id,
    #        is_published=True,
    #    )
    # )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes.first().category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, pk=id, is_published=True,)

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
