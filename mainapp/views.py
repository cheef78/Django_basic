from django.shortcuts import render
from django.conf import settings
from mainapp.models import Product, ProductCategory
from django.shortcuts import get_object_or_404
from basketapp.models import Basket
import os
import json

# Create your views here.

def main (request):
    products = Product.objects.all()[:4]
    basket = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat = True)))
    
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Главная',
        'products' : products,
        'basket' : basket,

    }
    return render (request, 'mainapp/index.html', content)

""" def products (request, pk = None):
   
    links_menu = [
        {'href':'products_all', 'name':'Все'},
        {'href':'products_home', 'name':'Для дома'},
        {'href':'products_office', 'name':'Для офиса'},
        {'href':'products_modern', 'name':'Современный стиль'},
        {'href':'products_classic', 'name':'Классический стиль'}
    ] 
    links_menu = ProductCategory.objects.all()
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Каталог',
        'links_menu': links_menu
    }
    return render (request, 'mainapp/products.html', content) """

def contact (request):
    basket = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat = True)))
    
    contacts_data = []
    with open (os.path.join(settings.BASE_DIR, 'contacts.json'), 'r', encoding='utf-8') as f:
        contacts_data = json.load(f)
    print (f)

    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Контакты',
        'contacts_data' : contacts_data,
        'basket' : basket,
    }
    return render (request, 'mainapp/contact.html', content)



def products (request, pk=None):
    print(pk)
    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = 0
    if request.user.is_authenticated:
        basket = sum(list(Basket.objects.filter(user=request.user).values_list('quantity', flat = True)))
        print (basket)
    if pk is not None:
        if pk == 0:
            products = Product.objects.all().order_by( 'price' )
            category = { 'name' : 'все' }
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by( 'price' )
        content = {
            'title' : title,
            'links_menu' : links_menu,
            'category' : category,
            'products' : products,
            'basket' : basket,
            'some_name' : 'Oleg Suslov',
        }
        return render(request, 'mainapp/products_list.html' , content)
    same_products = Product.objects.all()[ 3 : 5 ]
    content = {
        'title' : title,
        'links_menu' : links_menu,
        'same_products' : same_products,
        'basket' : basket,
        'some_name' : 'Oleg Suslov',
    }
    return render(request, 'mainapp/products.html' , content)