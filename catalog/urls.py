from django.urls import path
from catalog.views import contacts, HomeListView, ProductDetailView
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('contacts/', contacts, name='contacts'),
    # path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='product'),
]
