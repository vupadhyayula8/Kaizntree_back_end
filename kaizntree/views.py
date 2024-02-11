from django.shortcuts import render
from kaizntree.dbModels import *
import json
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from django.core.servers.basehttp import WSGIServer
WSGIServer.handle_error = lambda *args, **kwargs: None

# Create your views here.
# client = MongoClient('MONGO_CONNECTION_STRING')
# db = client['DB_NAME']

def healthcheck(request):
    print('hello')

def login(request):
    # UserDetails(username="allen", password="hhhhhhh").save()
    response = 'false'

    if request.method == "POST":
        data = json.loads((request.body).decode("utf-8"))

        if data["username"] and data["password"]:
            if len(UserDetails.objects(username=data['username'])) > 0:
                print('\n\n\n', UserDetails.objects(username=data["username"])[0].username == data["username"], check_password(data['password'], UserDetails.objects(username=data["username"])[0].password), '\n\n\n')
                if UserDetails.objects(username=data["username"])[0].username == data["username"] and check_password(data['password'], UserDetails.objects(username=data["username"])[0].password):
                    response = 'true'
                
            # UserDetails(username=data["username"], password=make_password(data["password"])).save()
    return HttpResponse(response)

def register(request):
    response = 'false'

    if request.method == "POST":
        data = json.loads((request.body).decode("utf-8"))

        if data["username"] and data["password"]:
            if len(UserDetails.objects(username=data['username'])) == 0:
                UserDetails(username=data['username'], password=make_password(data['password'])).save()
                response = 'true'

                return response
            else:
                return response
        
    return response

def fetch_items(request):
    return HttpResponse("Fetch items")


def add_item(request):
    return HttpResponse("Add item")


def add_category(request):
    return HttpResponse("Add category")
