from django.shortcuts import render
from django.http import HttpResponse

from food.models import Item


def index(request):
    items = Item.objects.all()
    context = {'item_list': items,}
    return render(request, 'food/index.html', context)

def item(request):
    return render(request, 'food/item.html')

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item,}
    return render(request, 'food/detail.html', context)
