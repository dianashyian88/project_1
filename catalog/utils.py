from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_categories_cache():
    key = 'category_list'

    if CACHE_ENABLED:
       return cache.get(key)

    category_list = Category.objects.all()
    if CACHE_ENABLED:
        cache.set(key, category_list)

    return category_list
