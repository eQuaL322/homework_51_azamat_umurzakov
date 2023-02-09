from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat


def view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'cat_stats.html')
    Cat.cat_info(request)
    Cat.name = Cat.get_name(request)
    context = {
        'name': Cat.name,
        'age': Cat.age,
        'happines': Cat.happines,
        'satiety': Cat.satiety,
        'mood': Cat.cat_mood,
    }
    return render(request, 'cat_stats.html', context=context)
