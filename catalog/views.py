from django.shortcuts import render
from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list,
        'title': 'Каталог'
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def product(request, pk):
    products_list = Product.objects.get(pk=pk)
    context = {
        'object_list': products_list,
        'title': 'Карточка продукта'
    }
    return render(request, 'catalog/product.html', context)
