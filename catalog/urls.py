from django.urls import path
from catalog.views import contacts, categories, HomeListView, ProductDetailView, ProductCreateView, ProductUpdateView,\
    StoryCreateView, StoryListView, StoryDetailView, StoryUpdateView, StoryDeleteView, ProductManagersUpdate
from catalog.apps import CatalogConfig
from django.views.decorators.cache import cache_page

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    path('categories/', categories, name='categories'),
    path('product_create/', ProductCreateView.as_view(), name='product_form'),
    path('product/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product'),
    path('product_edit/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('product_edit/<int:pk>', ProductManagersUpdate.as_view(), name='managers_product_update'),
    path('create/', StoryCreateView.as_view(), name='story_form'),
    path('story/', StoryListView.as_view(), name='story_list'),
    path('view/<int:pk>', StoryDetailView.as_view(), name='story_detail'),
    path('edit/<int:pk>', StoryUpdateView.as_view(), name='story_update'),
    path('delete/<int:pk>', StoryDeleteView.as_view(), name='story_delete'),

]
