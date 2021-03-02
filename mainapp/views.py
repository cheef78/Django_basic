from django.shortcuts import render

# Create your views here.

def main (request):
    content = {
        'some_name' : 'Oleg',
        'some_condition' : 0,
        'variable1' : 'YA YA',
        'variable2' : 'NO NO',
        'item_list' : ['basik', 'CS_GO', 'MS_Oficce']
    }
    return render (request, 'mainapp/index.html', content)

def products (request):
    return render (request, 'mainapp/products.html')

def contact (request):
    return render (request, 'mainapp/contact.html')
