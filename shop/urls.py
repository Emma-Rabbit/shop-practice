from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.products, name='products'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('addToCart', views.add_to_cart, name='addToCart'),
    path('cart', views.cart, name='cart'),
    path('removeFromCart', views.remove_from_cart, name='removeFromCart'),
]