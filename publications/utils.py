from django.db.models import Count
from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Напишите нам', 'url_name': 'add_page'},
        {'title': 'Контакты', 'url_name': 'contact'},
        {'title': 'Магазин товаров', 'url_name': 'shop'},
        ]


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        rubrics = RubricPublications.objects.annotate(Count('publications'))
        context['menu'] = menu
        context['rubrics'] = rubrics
        if 'rubric_selected' not in context:
            context['rubric_selected'] = 0
        return context
