from mongoengine import *
import os

# connect(host=os.getenv('MONGO_CONNECTION_STRING'))
connect(host=os.getenv('MONGO_CONNECTION_STRING'))

class UserDetails(Document):
    username = StringField()
    password = StringField()

    meta = {'collection': 'UserDetails'}

class Category(Document):
    categoryName = StringField()

    meta = {'collection': 'Catgories'}

class Tag(Document):
    tagName = StringField()

    meta = {'collection': 'Tags'}

class Item(Document):
    sku = StringField()
    name = StringField()
    tags = ListField(ReferenceField(Tag))
    category = ReferenceField(Category)
    inStock = DecimalField()
    availableStock = DecimalField()

    meta = {'collection': 'Items'}

class UserItems(Document):
    username = ReferenceField(UserDetails)
    items = ListField(ReferenceField(Item))

    meta = {'collection': 'UserItems'}