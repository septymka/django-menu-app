from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse

from food.models import Item


def index(request):
    items = Item.objects.all()
    return HttpResponse(items)

def item(request):
    return HttpResponse('<h1>This is an item view.</h1>')
