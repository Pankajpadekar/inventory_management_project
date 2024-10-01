from django.shortcuts import render
from rest_framework.response import Response
from .models import Item
from .serializers import ItemSerialzer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.core.cache import cache
# Create your views here.


class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer = ItemSerialzer
    permission_classes = [IsAuthenticated]


class ItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer = ItemSerialzer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        item_id = kwargs['pk']
        cache_key = f"item_{item_id}"
        cached_item = cache.get(cache_key)

        if cached_item:
            return Response(cached_item)

        else:
            response = super().get(request, *args, **kwargs)
            cache.get(cache_key, response.data, timeout=60*10)
            return response
