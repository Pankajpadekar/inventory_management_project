from django.db import models

# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    added_on = models.DateField(auto_now_add= True)
    updated_on = models.DateTimeField(auto_now=True)