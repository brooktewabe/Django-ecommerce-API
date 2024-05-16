# convert instances of Items from objects(JSON) into data types that 
# the response can understand

from . import models
from rest_framework import serializers
from rest_framework.fields import CharField, EmailField


# from .models import Item
# class ItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= Item
#         fields= '__all__'

class ContactSerializer(serializers.ModelSerializer):

	name = CharField(source="title", required=True)
	message = CharField(source="description", required=True)
	email = EmailField(required=True)
	
	class Meta:
		model = models.Contact
		fields = (
			'name',
			'email',
			'message'
		)