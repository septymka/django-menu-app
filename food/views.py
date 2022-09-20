from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from food.models import Item
from food.forms import ItemForm



class IndexClassView(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'


class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'


class CreateItem(CreateView):
    model = Item
    fields = ['name', 'description', 'price', 'image']
    template_name = 'food/item-form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def update_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')

    context = {
        'form': form,
        'item': item,
    }

    return render(request, 'food/item-form.html', context)

def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('food:index')

    context = {'item': item}
    return render(request, 'food/item-delete.html', context)
