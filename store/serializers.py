# convert instances of Items from objects into data types that the response can understand

from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model= Item
        fields= '__all__'