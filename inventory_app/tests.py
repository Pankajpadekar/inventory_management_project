from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Item

class ItemTest(APITestCase):
    def test_item(self):
        url = reverse('item-create')
        data = {'name' : 'Lenovo', 'description' : 'Laptop manufacturing Company'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
