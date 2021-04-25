from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlencode, urlunparse
import requests
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from authapp.models import ShopUserProfile
from authapp.models import ShopUser
from urllib.request import urlretrieve
from django.conf import settings

def save_user_profile(backend, user, response, *args, **kwargs):
    if backend.name != 'vk-oauth2':
        return
    
    api_url = f"https://api.vk.com/method/users.get?fields=bdate,sex,about,photo_max&access_token={response['access_token']}&v=5.92"
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return
    data = resp.json()['response'][0]
    if data['sex']:
        user.shopuserprofile.gender = ShopUserProfile.MALE if data['sex'] == 2 else ShopUserProfile.FEMALE
    if data['about']:
        user.shopuserprofile.aboutMe = data['about']
    if data['photo_max']:
        out = (settings.MEDIA_ROOT + '\\users_avatars\\' + user.username + ".jpg")
        urlretrieve(data['photo_max'], out)
        user.avatar = out
   
    if data['bdate']:
        bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()
        age = timezone.now().date().year - bdate.year
        user.age = age 
        if age < 18:
            user.delete()
            raise AuthForbidden('social_core.backends.vk.VKOAuth2')
    user.save()