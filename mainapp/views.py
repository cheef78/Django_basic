from django.shortcuts import render
from django.conf import settings
from mainapp.models import Product, ProductCategory

import os
import json

# Create your views here.

def main (request):
    products = Product.objects.all()[:4]
    
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Главная',
        'products' : products
    }
    return render (request, 'mainapp/index.html', content)

def products (request, pk = None):
   
    """ links_menu = [
        {'href':'products_all', 'name':'Все'},
        {'href':'products_home', 'name':'Для дома'},
        {'href':'products_office', 'name':'Для офиса'},
        {'href':'products_modern', 'name':'Современный стиль'},
        {'href':'products_classic', 'name':'Классический стиль'}
    ] """
    links_menu = ProductCategory.objects.all()
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Каталог',
        'links_menu': links_menu
    }
    return render (request, 'mainapp/products.html', content)

def contact (request):
    
    contacts_data = []
    with open (os.path.join(settings.BASE_DIR, 'contacts.json'), 'r', encoding='utf-8') as f:
        contacts_data = json.load(f)
    print (f)

    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Контакты',
        'contacts_data' : contacts_data
    }
    return render (request, 'mainapp/contact.html', content)
