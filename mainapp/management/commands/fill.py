import os
import json
from django.core.management import BaseCommand
from django.conf import settings
from mainapp.models import ProductCategory

def load_from_json(file_name):
    with open(os.path.join (settings.BASE_DIR, f'mainapp/json/{file_name}.json'), 'r', encoding='utf-8') as f:
        return json.load(f)




class Command (BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categories')
        # print (categories)
        ProductCategory.objects.all().delete()
        for cat in categories:
            ProductCategory.objects.create(**cat)


