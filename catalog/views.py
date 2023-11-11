from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from catalog.models import Product, Story, Category
from django.urls import reverse_lazy, reverse
from pytils.translit import slugify
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from catalog.utils import get_categories_cache


class HomeListView(ListView):
    model = Product
    template_name = 'catalog/home.html'


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


def categories(request):
    context = {
        'object_list': get_categories_cache(),
        'title': 'Все категории Чудо-магазина'
    }
    return render(request, 'catalog/categories.html', context)

class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'catalog/product.html'


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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price')
    success_url = reverse_lazy('catalog:home')

    def form_valid(self, form):
        self.object = form.save()
        self.object.owner = self.request.user
        self.object.save()

        return super().form_valid(form)

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    fields = ('name', 'description', 'image', 'category', 'price',)
    #permission_required = 'catalog.change_product'

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.object.owner != self.request.user and not self.request.user.is_staff:
            raise Http404
        return self.object

class ProductManagersUpdate(PermissionRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ('description', 'category', 'is_published',)
    permission_required = 'catalog.change_product'

    def form_valid(self, form):
        if form.is_valid():
            new_product = form.save()
            new_product.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('catalog:product', args=[self.kwargs.get('pk')])

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if not self.request.user.is_staff:
            raise Http404
        return self.object
