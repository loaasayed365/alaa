from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    products = Product.objects.all()
    category = request.GET.get('category')
    if category:
        products = products.filter(product_category=category)
    return render(request, 'home/index.html',{'products':products})

def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    return render(request, 'home/product_detail.html',{'product':product})