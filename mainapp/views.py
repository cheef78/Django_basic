from django.shortcuts import render
from django.conf import settings
import os
import json

# Create your views here.

def main (request):
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Главная'
    }
    return render (request, 'mainapp/index.html', content)

def products (request):
    links_menu = [
        {'href':'products_all', 'name':'Все'},
        {'href':'products_home', 'name':'Для дома'},
        {'href':'products_office', 'name':'Для офиса'},
        {'href':'products_modern', 'name':'Современный стиль'},
        {'href':'products_classic', 'name':'Классический стиль'}
    ]
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Каталог',
        'links_menu': links_menu
    }
    return render (request, 'mainapp/products.html', content)

def contact (request):
    """ contacts_data = [
    {
    'city':'Москва',
    'phone':'+7-888-888-8888',
    'email':'info_msk@geekshop.ru',
    'adress':'Алтуфьевское шоссе, д.16'
    },
    {
        'city':'Иркутск',
        'phone':'+7-395-248-15425',
        'email':'info_ikt@geekshop.ru',
        'adress':'ул. Степана Разина, д.14, оф.34'
    },
    {
        'city':'Сочи',
        'phone':'+7-124-548-7265',
        'email':'info_sochi@geekshop.ru',
        'adress':'Олимпийский проспект, д.24'
    },
    {
        'city':'Караганда',
        'phone':'+7-666-435-3952',
        'email':'info_karaganda@geekshop.ru',
        'adress':'Печальная улица, д.45'
    } 
    ]"""
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
