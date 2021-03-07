from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(unique=True, verbose_name='имя', max_length=64)
    descript = models.TextField(verbose_name='описание', blank=True )

    def __str__(self):
        return self.name
    

class Product(models.Model):

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя', max_length=128)
    image = models.ImageField(blank = True, upload_to='products_images')
    short_desc = models.CharField(verbose_name='краткое описание', max_length=64, blank=True)
    descript = models.TextField(blank=True, verbose_name='полное описание')
    price = models.DecimalField(verbose_name='цена, руб.', decimal_places=0, max_digits=8, default=0)
    quantity = models.SmallIntegerField(verbose_name='количество на складе, шт.', default=0)


    def __str__(self):
        return f'{self.name} ({self.category.name})'
            
