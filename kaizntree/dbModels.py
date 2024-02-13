from mongoengine import *
from rest_framework import serializers
import os

# connect(host=os.getenv('MONGO_CONNECTION_STRING'))

class UserDetails(Document):
    username = StringField()
    password = StringField()

    meta = {'collection': 'UserDetails'}

class UserDetailsSerializer(serializers.Serializer):
    # initialize fields
    username = serializers.CharField()
    password = serializers.CharField()

class Category(Document):
    categoryName = StringField()

    meta = {'collection': 'Catgories'}

class CategorySerializer(serializers.Serializer):
    categoryName = serializers.CharField()

class Tag(Document):
    tagName = StringField()

    meta = {'collection': 'Tags'}

class TagSerializer(serializers.Serializer):
    tagName = serializers.CharField()

class Item(Document):
    sku = StringField()
    name = StringField()
    tags = ListField(ReferenceField(Tag))
    category = ReferenceField(Category)
    inStock = DecimalField()
    availableStock = DecimalField()

    meta = {'collection': 'Items'}

class ItemSerializer(serializers.Serializer):
    sku = serializers.CharField()
    name = serializers.CharField()
    tags = TagSerializer(many=True)
    category = CategorySerializer()
    inStock = serializers.DecimalField(max_digits=10, decimal_places=2)
    availableStock = serializers.DecimalField(max_digits=10, decimal_places=2)

class UserItems(Document):
    username = ReferenceField(UserDetails)
    items = ListField(ReferenceField(Item))

    meta = {'collection': 'UserItems'}

class UserItemsSerializer(serializers.Serializer):
    username = UserDetailsSerializer()
    items = ItemSerializer(many=True)