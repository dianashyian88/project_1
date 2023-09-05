from django.shortcuts import render
from catalog.models import Product


def home(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list
    }
    return render(request, 'catalog/home.html', context)


def contacts(request):
    return render(request, 'catalog/contacts.html')


def product(request):
    products_list = Product.objects.all()
    context = {
        'object_list': products_list[0]
    }
    return render(request, 'catalog/product.html', context)
