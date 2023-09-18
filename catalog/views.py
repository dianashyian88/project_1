from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Story
from django.urls import reverse_lazy


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


# def home(request):
#     products_list = Product.objects.all()
#     context = {
#         'object_list': products_list,
#         'title': 'Каталог'
#     }
#     return render(request, 'catalog/home.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product.html'


# def product(request, pk):
#     products_list = Product.objects.get(pk=pk)
#     context = {
#         'object_list': products_list,
#         'title': 'Карточка продукта'
#     }
#     return render(request, 'catalog/product.html', context)

class StoryCreateView(CreateView):
    model = Story
    fields = ('title', 'slug', 'body', 'image', 'public_flg', 'views_count',)
    success_url = reverse_lazy('catalog:story_list')


class StoryListView(ListView):
    model = Story


class StoryDetailView(DetailView):
    model = Story


class StoryUpdateView(UpdateView):
    model = Story
    fields = ('title', 'slug', 'body', 'image', 'public_flg', 'views_count',)
    success_url = reverse_lazy('catalog:story_list')


class StoryDeleteView(DeleteView):
    model = Story
    success_url = reverse_lazy('catalog:story_list')
