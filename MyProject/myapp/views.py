from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.forms import *
from myapp.models import *
from django.contrib import messages

# Create your views here.

def index(request):
    card = Product.objects.all()
    return render(request, 'myapp/index.html', {'info': card})

def addProduct(request):
    form = AddProductForm
    if request.method == "POST":
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("index")
    return render(request,'myapp/addProduct.html', {"form": form})

def createCart(request):
    cart_user = 1
    cart = Cart()
    cart.create
    cart.save()

def addCart(request, id):
    cart_user = 1
    cart = Cart.objects.get(id_user=cart_user)
    quantidade = 1
    add = CartItem(product=id, quantidade = quantidade, cart = cart.id)
    add.save()

def edit(request, id):
    item = Product.objects.get(pk=id)
    form = AddProductForm(instance=item)
    return render(request, "myapp/update.html",{"form":form, "item":item})


def update(request, id):
    try:
        if request.method == "POST":
            item = Product.objects.get(pk=id)
            form = AddProductForm(request.POST, request.FILES, instance=item)
            
            if form.is_valid():
                form.save()
                messages.success(request, 'item foi alterada com sucesso!')
                return redirect('index')
    except Exception as e:
        messages.error(request, e)
        return redirect('index')
            

def read(request, id):
    item = Product.objects.get(pk=id)
    return render(request, "myapp/read.html", {"item":item})

def delete(request, id):
    item = Product.objects.get(pk=id)
    item.delete()
    messages.success(request, 'item foi deletada com sucesso!')
    return redirect('index')

def listar(request):
    card = Product.objects.all()
    return render(request, 'myapp/listar.html', {'info': card})