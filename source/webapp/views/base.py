from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render

from webapp.cat import Cat


def index_view(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'index.html')
    else:
        Cat.name = Cat.get_name(request)
        return render(request, 'cat_stats.html', context={
            'name': Cat.name,
            'age': Cat.age,
            'happines': Cat.happines,
            'satiety': Cat.satiety,
            'mood': Cat.cat_mood,
        })
