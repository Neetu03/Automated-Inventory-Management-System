from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from django.dispatch import receiver, Signal
from .signals import sell_product



def home_page(request):
    if request.method=="POST":
        product = request.POST
        product_name=product.get('product_name')
        Price=product.get('Price')
        Category=product.get('Category')
        Quantity=product.get('Quantity')
        if not Products.objects.filter(product_name=product_name).exists():
            p=Products(product_name=product_name,Price=Price,
            Category=Category,Quantity=Quantity)
            p.save()
        else:
            messages.info(request, "This Product Already Exists")

        return redirect('/')
    query=Products.objects.all()
    return render(request,"home.html",{'products':query})

def Sell_p(request,id):
    if request.method=="POST":
        q=int(request.POST.get("Quantity"))
        current_product=Products.objects.get(id=id)
        amount=current_product.Quantity
        new_amount = amount - q
        current_product.Quantity = new_amount
        current_product.save()
        # sell_product.send(sender=Products, instance=current_product, created=False)
        messages.success(request, "Product Sold")
        return redirect('/')

    return render(request,"sell.html")

def Buy_p(request,id):
    if request.method=="POST":
        q=int(request.POST.get("Quantity"))
        current_product=Products.objects.get(id=id)
        amount=current_product.Quantity
        new_amount = amount + q
        current_product.Quantity = new_amount
        current_product.save()
        # ProductID=current_product.id
        t=transactions(
                        ProductID=current_product,
                        TransactionType="IN",
                        Quantity=q,
                        Category=current_product.Category)
        t.save()
        messages.success(request, "Product Bought")
        return redirect('/')
    return render(request,"buy.html")

def update_p(request,id):
    product=Products.objects.get(id=id)
    if request.method=="POST":
        new_product_Category=request.POST.get('Category')
        new_product_Price=request.POST.get('Price')
        new_product_Quantity=request.POST.get('Quantity')
        new_product_product_name=request.POST.get('product_name')
        product.Category=new_product_Category
        product.Price=new_product_Price
        product.Quantity=new_product_Quantity
        product.product_name=new_product_product_name
        product.save()
        messages.success(request,"Product Successfully Updated")
        return redirect('/')
    return render(request,"update.html",{'product':product})

def delete_p(request,id):
    p=Products.objects.filter(id=id)
    p.delete()
    return redirect('/')

def transactions_page(request):
    trans=transactions.objects.all()
    return render(request, "transactions.html",{'trans':trans})