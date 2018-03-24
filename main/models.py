from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.forms import ModelForm,Textarea, ChoiceField
from django import forms
# Create your models here.
OCENKI = [(i, str(i)) for i in range(1, 6)]
class BigCategory(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:MainCategory', args=[self.slug])
    
    

class Category_notebook(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    category = models.ForeignKey(BigCategory, related_name='category', verbose_name='Категории', null=True)
    prop_list = models.TextField(blank=True)
    

    class Meta:
        ordering = ['name']
        verbose_name = 'Подкатегория товара'
        verbose_name_plural = 'Подкатегории товаров'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:NotebookSListByCategory', args=[self.slug])


class PhotoPack(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id']
        ]
    def __str__(self):
        return self.name

    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение")
    categoria = models.ForeignKey(BigCategory, verbose_name="Категория", null=True)


class HubNotebook(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return self.name

    maincategory = models.ForeignKey(BigCategory, related_name='hubnotes', verbose_name='Хаб', null=True)
    category = models.ForeignKey(Category_notebook, related_name='notebooks', limit_choices_to={'category': 1},
                                 verbose_name='ГруппаНоутбуков', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image_array = models.ManyToManyField(PhotoPack, limit_choices_to={'categoria':1},blank=True, null=True)

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.slug])

class HubPC(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return self.name

    maincategory = models.ForeignKey(BigCategory, related_name='hubpc', verbose_name='ХабPC', null=True)
    category = models.ForeignKey(Category_notebook, related_name='pc', limit_choices_to={'category': 5},
                                 verbose_name='ГруппаPC', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.slug])


class HubComplecting(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return self.name

    maincategory = models.ForeignKey(BigCategory, related_name='hubcomplecting', verbose_name='ХабКомплектуюшие', null=True)
    category = models.ForeignKey(Category_notebook, related_name='hubcomplecting_category', limit_choices_to={'category': 2},
                                 verbose_name='ГруппаКОмплектующие', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.slug])

class HubAcses(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return self.name

    maincategory = models.ForeignKey(BigCategory, related_name='hubacses', verbose_name='ХабАксессуары', null=True)
    category = models.ForeignKey(Category_notebook, related_name='hubacses_categoty', limit_choices_to={'category': 4},
                                 verbose_name='ГруппаАксес', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.slug])

class HubPerf(models.Model):
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
    def __str__(self):
        return self.name

    maincategory = models.ForeignKey(BigCategory, related_name='hubperf', verbose_name='ХабПереферия', null=True)
    category = models.ForeignKey(Category_notebook, related_name='hubperf_category', limit_choices_to={'category': 3},
                                 verbose_name='ГруппаПереферия', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.slug])


class Notebook(models.Model):
    maincategory = models.ForeignKey(BigCategory,related_name='maincat', verbose_name='Раздел',null=True)
    category = models.ForeignKey(Category_notebook, related_name='notebook', limit_choices_to={'category':1 }, verbose_name='Ноутбуки')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    property_2 = models.CharField(max_length=200, db_index=True, verbose_name="Процессор")
    property_3 = models.CharField(max_length=200, db_index=True, verbose_name="RAM")
    property_4 = models.CharField(max_length=200, db_index=True, verbose_name="Видеокарта")
    property_5 = models.CharField(max_length=200, db_index=True, verbose_name="Память")
    property_6 = models.CharField(max_length=200, db_index=True, verbose_name="Экран", null=True)
    property_1 = models.CharField(max_length=200, db_index=True, verbose_name="Производитель",null=True)
    hub = models.ForeignKey(HubNotebook, related_name= 'hub', verbose_name='Модель', null=True)
    details = models.TextField(blank=True, verbose_name="Описание")
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.hub.id])

class Complecting(models.Model):
    maincategory = models.ForeignKey(BigCategory, related_name='maincat1', verbose_name='Раздел',null=True)
    category = models.ForeignKey(Category_notebook, related_name='complecting', limit_choices_to={'category':2 }, verbose_name='Комплюктующие')
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    property_1 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 1")
    property_2 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 2")
    property_3 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 3")
    property_4 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 4")
    property_5 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 5")
    details = models.TextField(blank=True, verbose_name="Описание")
    hub = models.ForeignKey(HubComplecting, related_name='hub', verbose_name='Модель', null=True)
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug,self.category.slug, self.hub.id])
    

    
class Perf(models.Model):
    maincategory = models.ForeignKey(BigCategory, related_name='maincat3', verbose_name='Раздел',null=True)
    category = models.ForeignKey(Category_notebook, related_name='perf',limit_choices_to={'category':3 }, verbose_name='Переферия', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    property_1 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 1")
    property_2 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 2")
    property_3 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 3")
    property_4 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 4")
    details = models.TextField(blank=True, verbose_name="Описание")
    hub = models.ForeignKey(HubPerf, related_name='hub', verbose_name='Модель', null=True)
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug,self.category.slug, self.hub.id])
    
    
class Acses(models.Model):
    maincategory = models.ForeignKey(BigCategory, related_name='maincat4', verbose_name='Раздел',null=True)
    category = models.ForeignKey(Category_notebook, limit_choices_to={'category':4 }, related_name='acses', verbose_name='Аксесуары', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    property_1 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 1")
    property_2 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 2")
    property_3 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 3")
    property_4 = models.CharField(max_length=200, db_index=True, verbose_name="Свойство 4")
    details = models.TextField(blank=True, verbose_name="Описание")
    hub = models.ForeignKey(HubAcses, related_name='hub', verbose_name='Модель', null=True)
    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug,self.category.slug, self.hub.id])

class ProductStat(models.Model):
    class Meta:
            db_table = "ProductStat"

    product_slug = models.CharField(max_length=200, db_index=True, verbose_name='Что?', null=True)
    product_cat = models.CharField(max_length=200, db_index=True, verbose_name='Откуда?', null=True)
    date = models.DateField('Дата', default=timezone.now())
    views = models.IntegerField('Просмотры', default=0)


    def __str__(self):
        return self.product_slug

class ShakeProduct(models.Model):
    maincategory = models.ForeignKey(BigCategory, related_name='maincatshake', verbose_name='Раздел',null=True)
    categoty = models.ForeignKey(Category_notebook, related_name='catshake', verbose_name='Подразде', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Товарик')

class Utility(models.Model):
    name = models.CharField(max_length=200, db_index=True,verbose_name='Название1')
    value = models.CharField(max_length=200, db_index=True, verbose_name='Значение1')

class PC(models.Model):
    maincategory = models.ForeignKey(BigCategory, related_name='maincat5', verbose_name='Раздел', null=True)
    category = models.ForeignKey(Category_notebook, limit_choices_to={'category':5 }, related_name='PC', verbose_name='Компьютеры', null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    property_1 = models.ForeignKey(Complecting, limit_choices_to={'category':4 },verbose_name="Процессор", related_name='CPU')
    property_2 = models.ForeignKey(Complecting, limit_choices_to={'category':6 },verbose_name="RAM", related_name='RAM')
    property_3 = models.ForeignKey(Complecting, limit_choices_to={'category':5 },verbose_name="Видеокарта", related_name='Video')
    property_4 = models.ForeignKey(Complecting, limit_choices_to={'category':3 },verbose_name="Память", related_name='Memory' )
    property_5 = models.ForeignKey(Complecting, limit_choices_to={'category':27 },verbose_name="Материнска плата", related_name='Motherboard')
    property_6 = models.ForeignKey(Complecting, limit_choices_to={'category':29 },verbose_name="Блок питания/Кейс", related_name='BP')
    property_7 = models.ForeignKey(Complecting, limit_choices_to={'category':29 }, verbose_name="Блок питания/Кейс", null=True, related_name='Case')
    property_8 = models.ForeignKey(Complecting, limit_choices_to={'category':30 } , verbose_name="Система охлождения", null=True, related_name='Cooler')
    property_9 = models.ForeignKey(Complecting, limit_choices_to={'category':28 }, verbose_name="DVD", null=True, related_name='DVD')
    perf_list  = models.ManyToManyField(Perf)
    acses_list = models.ManyToManyField(Acses)
    hub = models.ForeignKey(HubPC, related_name='hubPC', verbose_name='МодельPC', null=True)
    details = models.TextField(blank=True, verbose_name="Описание")

    def get_perf_price(self):
        price = 0
        for perf_item in self.perf_list.all():
            price += perf_item.price
        return price

    def get_acses_price(self):
        price = 0
        for acses_item in self.acses_list.all():
            price += acses_item.price
        return price

    def get_absolute_url(self):
        return reverse('main:ProductDetail', args=[self.maincategory.slug, self.category.slug, self.hub.id])

class PCForm(ModelForm):
    class Meta:
        model=PC
        fields=['property_1','property_2','property_3','property_4','property_5','property_6','property_7','property_8','property_9']
        widgets = {
            'name': Textarea(attrs={'cols': 80, 'rows': 20})}




class Reviews(models.Model):
    class Meta:
        db_table = "reviews"

    author = models.CharField(max_length=200, verbose_name='Ваше имя')
    review = models.TextField(verbose_name='Ваше отзыв')
    category = models.CharField(max_length=200)
    product = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    ocenka = models.IntegerField(verbose_name='Оценка')


class ReviewsForm(ModelForm):
    class Meta:
        model=Reviews
        fields=['author','review','ocenka']
        widgets = {
            'ocenka': forms.Select(choices=OCENKI)
        }