from django.shortcuts import render
from kaizntree.dbModels import *
import json
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.core.servers.basehttp import WSGIServer
WSGIServer.handle_error = lambda *args, **kwargs: None
from django.http import JsonResponse
from rest_framework import serializers
from django.contrib.auth import authenticate
# from django_mongoengine.django.auth import User

# Create your views here.
# client = MongoClient('MONGO_CONNECTION_STRING')
# db = client['DB_NAME']

def healthcheck(request):
    print('hello')

def login(request):
    res = HttpResponse(json.dumps({"status": False, 'msg': 'Invalid request'}), content_type="application/json")
    if request.method == "POST":
        data = json.loads((request.body).decode("utf-8"))

        if data["username"] and data["password"]:
            user_details = UserDetails.objects(username=data['username'])
            
            if len(user_details) == 1:
                if user_details[0].username == data["username"] and check_password(data['password'], user_details[0].password):
                    res = HttpResponse(json.dumps({"status": True, 'msg': 'User found', 'user_details': {"username": user_details[0].username}}), content_type="application/json")
    res.status_code = 201
    return res


def register(request):
    res = HttpResponse(json.dumps({"status": False, 'msg': "Username already exists"}))
    if request.method == "POST":
        data = json.loads((request.body).decode("utf-8"))

        if data["username"] and data["password"]:
            user_details = UserDetails.objects(username=data['username'])
            
            if len(user_details) == 0:
                UserDetails(username=data['username'], password=make_password(data['password'])).save()
                res = HttpResponse(json.dumps({"status": True, 'msg': 'User created'}))
    res.status_code = 201
    return res


def fetch_items(request):
    data = json.loads((request.body).decode("utf-8"))
    print(data['username'])
    user_details = UserDetails.objects(username=data['username']).get()
    print(user_details.username)
    print(user_details.id)
    if user_details:
        items = UserItems.objects(username=user_details.id)
        serializer = UserItemsSerializer(items)
        return JsonResponse(serializer.data)
        # print(items[0].username.username)
        # items_json = serializers.serialize('json', items)
        print(items)
    return HttpResponse(items)


def reset(request):
    return HttpResponse("reset password")


def add_item(request):
    return HttpResponse("Add item")


def add_category(request):
    return HttpResponse("Add category")