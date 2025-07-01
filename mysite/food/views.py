from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
# function based vieww
# def index(request):
#     item_list = Item.objects.all()
#     context = {
#         'item_list': item_list,
#     }
#     return render(request, 'food/index.html', context)

# class based views and list views
class IndexClassView(ListView):
    model = Item;
    template_name ='food/index.html'
    context_object_name = 'item_list'


def item(resquest):
    return HttpResponse("item page")


# detail views
class FoodDetails(DetailView):
    model = Item;
    template_name ='food/detail.html'



def create_item(request):
     form = ItemForm(request.POST or None)
     if form.is_valid():
         form.save()
         return redirect('index')
     return render(request, 'food/item_form.html', {'form': form})

# create item class based views
class CreateItem(CreateView):
    model = Item
    fields =['item_name','item_desc', 'item_image','item_price']
    template_name = 'food/item_form'
    
    def form_valid(self,form):
        form.instance.username = self.request.user
        
        return super().form_valid(form)

def update_item(request, item_id):
    item = Item.objects.get(id= item_id)
    form  = ItemForm(request.POST or None, instance= item)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'food/item_form.html', {'form': form, 'item': item})

def delete_item(request, item_id):
    item = Item.objects.get(id = item_id)

    if request.method == 'POST':
        item.delete()
        return redirect('index')
    return render(request, 'food/item_delete.html',{'item': item})