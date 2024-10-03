from django.urls import path
from .views import ItemCreateView, ItemDetailView

urlpatterns = [
    path('items/', ItemCreateView.as_view(), name='item-create'),  # For creating a new item
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),  # For retrieving an item
]
