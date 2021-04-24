from django.shortcuts import render
from authapp.forms import ShopUserLoginForm, ShopUserRegisterForm, ShopUserEditForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from authapp.models import ShopUser
# Create your views here.

def login(request):

    login_form = ShopUserLoginForm (data = request.POST)
    next = request.GET['next'] if 'next' in request.GET.keys() else ''

    if request.method == 'POST' and login_form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('main'))
            
    content = {
        'title':'Вход',
        'login_form':login_form,
        'next': next,
    }
    return render(request, 'authapp/login.html', content)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main'))
 
""" def register(request):
    
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm() 

    
    title = 'Регистрация'
    content = {'title': title, 'register_form': register_form}

    return render(request, 'authapp/register.html', content) 
"""

def edit(request):
    title = 'Редактирование'
    if request.method == 'POST':
        edit_form = ShopUserEditForm(request.POST, request.FILES, instance=request.user)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponseRedirect(reverse('auth:edit'))
    else:
        edit_form = ShopUserEditForm(instance=request.user)
    content = {'title': title, 'edit_form': edit_form}
    return render(request, 'authapp/edit.html', content)



def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.username, user.activation_key])
    title = f'Подтверждение учетной записи {user.username}'
    message = f'Для подтверждения учетной записи {user.username} на портале \
    {settings.DOMAIN_NAME} перейдите по ссылке:\n{settings.DOMAIN_NAME}{verify_link}'
    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)



def register(request):
    title = 'регистрация'
    
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)
        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('сообщение подтверждения отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('ошибка отправки сообщения')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()
    content = {'title': title, 'register_form': register_form}
    return render(request, 'authapp/register.html', content)

def verify(request, username, activation_key):
    try:
        user = ShopUser.objects.get(username=username)
        if user.activation_key == activation_key and not user.is_activation_key_expired():
            user.is_active = True
            user.activation_key = ''
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
        else:
            print(f'error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activation user : {e.args}')
        return HttpResponseRedirect(reverse('main'))
