from django.shortcuts import render
from .models import Item
from .serializers import ItemSerialzer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
# Create your views here.

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer
