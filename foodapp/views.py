from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render , redirect
from django.http import HttpResponse
from foodapp.models import Item
from foodapp.forms import ItemForm

def index(request):
    items_list = Item.objects.all()
    context = {'data':items_list,}
    return render(request,'food/index.html',context)

def details(request,item_id):
    item = Item.objects.get(pk=item_id)
    context = {"item":item,}
    return render(request,'food/details.html',context)

def add(request):
    if request.method == "POST":
        item_form = ItemForm(request.POST)
        if item_form.is_valid():
            item_form.save()
            return redirect('index')
    else:
        item_form = ItemForm()
    return render(request,'food/add.html',{"form":item_form})

def edit(request,id):
    item_obj = Item.objects.get(pk=id)
    item_form_obj = ItemForm(request.POST or None , instance=item_obj)
    if item_form_obj.is_valid():
        item_form_obj.save()
        return redirect('index')
    return render(request,'food/add.html',{'form':item_form_obj,'item':item_obj})

def delete(request,id):
    item_obj = Item.objects.get(pk=id)
    if request.method=="POST":
        item_obj.delete() 
        return redirect('index')
    return render(request,'food/delete.html',{'item':item_obj})

def support(request):
    return HttpResponse("support")

def contact(request):
    return HttpResponse("contact")

def report(request):
    return HttpResponse("report")

def compliments(request):
    return HttpResponse("compliments")

#Code for buttons edit and delete below the details button

# def delete(request,item_id):
#     get_item=Item.objects.get(pk=item_id)
#     get_item.delete()
#     return redirect('index')

# def edit(request,item_id):
#     if request.method== "POST":
#         item_form = ItemForm(request.POST)
#         if item_form.is_valid():
#             item_form.save()
#             return redirect('index')
#     else:
#         item = Item.objects.get(pk=item_id)
#         item_form = ItemForm(instance=item)
#     return render(request,'food/edit.html',{'form':item_form})