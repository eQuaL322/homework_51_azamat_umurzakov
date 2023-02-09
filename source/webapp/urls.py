from django.urls import path

from webapp.views.articles import view
from webapp.views.base import index_view

urlpatterns = [
    path('', index_view),
    path('cat_stats', view)
]
