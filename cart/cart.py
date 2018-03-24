from decimal import Decimal
from django.conf import settings
from main.models import Notebook, Complecting, Perf, Acses, Category_notebook, BigCategory, PC
from django.shortcuts import render, redirect, get_object_or_404


class Cart(object):
    def __init__(self, request):
        # Инициализация корзины пользователя
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохраняем корзину пользователя в сессию
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


        
    def add(self, product, quantity=1, update_quantity=False):
        product_name = str(product.slug)
        if product_name not in self.cart:
            self.cart[product_name] = {'quantity': 0,
                                       'price': str(product.price),
                                       'slug': str(product.slug),
                                       'big_cat': str(product.maincategory.slug)}
        if update_quantity:
            self.cart[product_name]['quantity'] = quantity
        else:
            self.cart[product_name]['quantity'] += quantity
        self.save()
        
    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        # Указываем, что сессия изменена
        self.session.modified = True
        
    def remove(self, product):
        product_slug = str(product)
        if product_slug in self.cart:
            del self.cart[product_slug]
            self.save()
          
    def __iter__(self):

        for item in self.cart.values():
            yield item




    # Количество товаров
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True



class Versus(object):
    def __init__(self, request):
        self.session = request.session
        versus = self.session.get(settings.VERSUS_SESSION_ID)
        if not versus:
            # Сохраняем корзину пользователя в сессию
            versus = self.session[settings.VERSUS_SESSION_ID] = {}
        self.versus = versus



    def save(self):
        self.session[settings.VERSUS_SESSION_ID] = self.versus
        # Указываем, что сессия изменена
        self.session.modified = True

    def clear(self):
        del self.session[settings.VERSUS_SESSION_ID]
        self.session.modified = True


    def versus_add(self,product,big_category_slug):
        category=big_category_slug
        extriminatus=False
        if self.versus.__len__() >= 2:
            for item in self.versus:
                varible=self.versus.__len__()
                if self.versus[item]['category'] != category:
                    extriminatus=True
        if extriminatus:
            self.versus={}
        if self.versus.__len__()>3:
            for item in self.versus:
                del self.versus[item]
                break

        if product not in self.versus:
            self.versus[product]={'name': str(product),'category' :  category}
        self.save()

    def __iter__(self):
        for item in self.versus.values():
            yield item

    def remove(self, product):
        product_slug = str(product)
        if product_slug in self.versus:
            del self.versus[product]
        self.save()


class Craft(object):
    def __init__(self, request):
        self.session = request.session
        craft = self.session.get(settings.CRAFT_SESSION_ID)
        if not craft:
            # Сохраняем корзину пользователя в сессию
            craft = self.session[settings.CRAFT_SESSION_ID] = {}
        self.craft = craft

    def save(self):
        self.session[settings.CRAFT_SESSION_ID] = self.craft
        # Указываем, что сессия изменена
        self.session.modified = True

    def clear(self):
        del self.session[settings.CRAFT_SESSION_ID]
        self.session.modified = True


    def craft_add(self,product,big_category_slug,category_slug):
        product_c=category_slug
        if big_category_slug=='komplektuyushie':
            if product_c=='motherboard':
                self.craft['motherboard']={'name':str(product)}
            if product_c=='cpu':
                self.craft['cpu']={'name':str(product)}
            if product_c=='video':
                self.craft['video']={'name':str(product)}
            if product_c=='ram':
                self.craft['ram']={'name':str(product)}
            if product_c=='hdd':
                self.craft['hdd']={'name':str(product)}
            if product_c=='dvd':
                self.craft['dvd']={'name':str(product)}
            if product_c=='coolers':
                self.craft['coolers']={'name':str(product)}
            if product_c=='bp':
                self.craft['bp_1']={'name':str(product)}
                self.craft['bp_2']={'name':str(product)}
        if big_category_slug == 'perf':
            if 'perf' not in self.craft:
                self.craft['perf']={}
            if product not in self.craft['perf']:
                self.craft['perf'][product] = {'name': str(product)}
        if big_category_slug == 'acses':
            if 'acses' not in self.craft:
                self.craft['acses']={}
            if product not in self.craft['acses']:
                self.craft['acses'][product] = {'name': str(product)}
        if big_category_slug=='kompyutery':
            product=get_object_or_404(PC, slug=product)
            self.craft['motherboard']={'name':str(product.property_5.slug)}
            self.craft['cpu']={'name':str(product.property_1.slug)}
            self.craft['video']={'name':str(product.property_3.slug)}
            self.craft['ram']={'name':str(product.property_2.slug)}
            self.craft['hdd']={'name':str(product.property_4.slug)}
            self.craft['dvd']={'name':str(product.property_9.slug)}
            self.craft['coolers']={'name':str(product.property_8.slug)}
            self.craft['bp_1']={'name':str(product.property_6.slug)}
            self.craft['bp_2']={'name':str(product.property_7.slug)}
            if 'acses' not in self.craft:
                self.craft['acses']={}
            for acses_item in product.acses_list.all():
                if acses_item not in self.craft['acses']:
                    self.craft['acses'][acses_item.slug] = {'name': str(acses_item)}
            if 'perf' not in self.craft:
                self.craft['perf'] = {}
            for perf_item in product.perf_list.all():
                if perf_item not in self.craft['perf']:
                    self.craft['perf'][perf_item.slug] = {'name': str(perf_item)}
        self.save()

    def __iter__(self):
        for item in self.craft.values():
            yield item

    def remove(self, product,big_category_slug):
        product_slug = str(product)
        if big_category_slug=='acses':
            if product_slug in self.craft['acses']:
                del self.craft['acses'][product_slug]
        if big_category_slug=='perf':
            if product_slug in self.craft['perf']:
                del self.craft['perf'][product_slug]
        if big_category_slug=='proc':
            del self.craft['cpu']
        if big_category_slug=='ram':
            del self.craft['ram']
        if big_category_slug=='video':
            del self.craft['video']
        if big_category_slug=='dvd':
            del self.craft['dvd']
        if big_category_slug=='bp_1':
            del self.craft['bp_1']
        if big_category_slug=='bp_2':
            del self.craft['bp_2']
        if big_category_slug=='cool':
            del self.craft['coolers']
        if big_category_slug=='matb':
            del self.craft['motherboard']
        if big_category_slug=='hdd':
            del self.craft['hdd']
        self.save()