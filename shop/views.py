from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, ProductInCart
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def index(request):
    return render(request, 'shop/index.html')

def products(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        product = Product(name=name, price=price)
        product.save()
        return redirect('/shop/products')
    if request.method == 'GET':
        products_list = Product.objects.all()
        template = loader.get_template('shop/products.html')
        context = {
            'products_list': products_list,
        }
        return HttpResponse(template.render(context, request))

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']        
        user = User.objects.create_user(name, email, password)
        user.save()
        return HttpResponse("user created")
    if request.method == 'GET':
       return render(request, 'shop/register.html')

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(request, username=name, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/shop')
        else:
            return HttpResponse("Wrong username or password")
    if request.method == 'GET':
        return render(request, 'shop/login.html')

def logout(request):
    auth_logout(request)
    return redirect('/shop')

def add_to_cart(request):
    if not request.user.is_authenticated:
        return redirect('/shop/login')
    product_id = request.POST['id']
    product = Product.objects.get(pk=product_id)
    user = request.user
    count = request.POST['count']
    pic = ProductInCart(user=user, product=product, count=count)
    pic.save()
    return redirect('/shop/products')