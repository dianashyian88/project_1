from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Story
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify


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
    fields = ('title', 'body', 'image', 'public_flg', 'views_count',)
    success_url = reverse_lazy('catalog:story_list')

    def form_valid(self, form):
        if form.is_valid():
            new_story = form.save()
            new_story.slug = slugify(new_story.title)
            new_story.save()

        return super().form_valid(form)


class StoryListView(ListView):
    model = Story

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(public_flg=True)
        return queryset


class StoryDetailView(DetailView):
    model = Story

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class StoryUpdateView(UpdateView):
    model = Story
    fields = ('title', 'body', 'image', 'public_flg', 'views_count',)
    #success_url = reverse_lazy('catalog:story_list')

    def form_valid(self, form):
        if form.is_valid():
            new_story = form.save()
            new_story.slug = slugify(new_story.title)
            new_story.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:story_detail', args=[self.kwargs.get('pk')])


class StoryDeleteView(DeleteView):
    model = Story
    success_url = reverse_lazy('catalog:story_list')
