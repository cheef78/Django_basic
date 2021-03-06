from django.shortcuts import render

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
    content = {
        'some_name' : 'Oleg Suslov',
        'title' : 'Контакты'
    }
    return render (request, 'mainapp/contact.html', content)
