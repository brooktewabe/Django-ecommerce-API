from django.db import models

class Item (models.Model):
    name= models.CharField(max_length=200)
    createdAt= models.DateTimeField(auto_now_add=True)