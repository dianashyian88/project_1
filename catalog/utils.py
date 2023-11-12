from catalog.models import Category
from config.settings import CACHE_ENABLED
from django.core.cache import cache

def get_categories_cache():
    # key = 'category_list'
    #
    # if CACHE_ENABLED:
    #     category_list = cache.get(key)
    #     if category_list is None:
    #         category_list = Category.objects.all()
    #         cache.set(key, category_list)
    # else:
    #     category_list = Category.objects.all()
    #
    # return category_list

    key = 'category_list'
    category_list = Category.objects.all()
    if CACHE_ENABLED:
        cache_category = cache.get(key)
        if cache_category is None:
            cache_category = category_list
            cache.set(key, cache_category)
        return cache_category
    else:
        return category_list
