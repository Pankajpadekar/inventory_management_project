from django.urls import path
from .views import ItemCreateView, ItemDetailView, ItemListView

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),  # For retrieving  all an item
    path('items/create/', ItemCreateView.as_view(), name='item-create'),  # For creating a new item
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),  # For retrieving an item
]
