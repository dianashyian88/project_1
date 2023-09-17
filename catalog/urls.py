from django.urls import path
from catalog.views import contacts, HomeListView, ProductDetailView, StoryCreateView, StoryListView, StoryDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    # path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
    path('create/', StoryCreateView.as_view(), name='story_form'),
    path('story/', StoryListView.as_view(), name='story_list'),
    path('story/<int:pk>', StoryDetailView.as_view(), name='story_detail'),

]
