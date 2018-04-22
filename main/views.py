from django.shortcuts import render, render_to_response, get_object_or_404
from .models import *
from cart.forms import CartAddProductForm
from django.utils import timezone
from django.db.models import Sum
from .forms import ChoisListForm
from django.db.models import Q
from collections import Counter
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def NotebookSList(request, category_slug):

# < !!! БЛОК ВЫБОРКИ ТОВАРОВ
    prop_list=[]
    if category_slug =='notebooks':
        products = Notebook.objects.all()
        title = 'Ноутбуки - PCShop.uz'
        prop_list = products[0].category.prop_list
        prop_list = prop_list.split(', ')
    elif category_slug =='komplektuyushie':
        products = Complecting.objects.all()
        title = 'Комплектующие - PCShop.uz'
    elif category_slug =='perf':
        products = Perf.objects.all()
        title = 'Периферия - PCShop.uz'
    elif category_slug =='acses':
        products = Acses.objects.all()
        title = 'Аксессуары - PCShop.uz'
    elif category_slug == 'pc':
        products = PC.objects.all()
        title = 'Компьютеры - PCShop.uz'
    else:
        categories = Category_notebook.objects.filter(slug=category_slug)
        title = str(categories[0]) + ' - PCShop.uz'
        if str(categories[0].category.slug) == 'notebooks':
            category = get_object_or_404(Category_notebook, slug=category_slug)
            products = Notebook.objects.filter(available=True,category=category)
        elif str(categories[0].category.slug) == 'komplektuyushie':
            category = get_object_or_404(Category_notebook, slug=category_slug)
            products = Complecting.objects.filter(available=True,category=category)
        elif str(categories[0].category.slug) == 'acses':
            category = get_object_or_404(Category_notebook, slug=category_slug)
            products = Acses.objects.filter(available=True,category=category)
        elif str(categories[0].category.slug) == 'perf':
            category = get_object_or_404(Category_notebook, slug=category_slug)
            products = Perf.objects.filter(available=True,category=category)
        prop_list = products[0].category.prop_list
        prop_list = prop_list.split(', ')
# КОНЕЦ БЛОКА ВЫБОРКИ ТОВАРОВ !!!!!>
    cart_product_form = CartAddProductForm()
# < !!! БЛОК ФОРМЫ ФИЛЬТРАЦИИ
    min_price = products.order_by('price').first().price
    max_price =  products.order_by('price').last().price
    p_1 = []
    p_2 = []
    p_3 = []
    p_4 = []
    p_5 = []
    p_6 = []


    for item in products:
        if item.property_1:
            p_1.append(str(item.property_1))
        if item.property_2:
            p_2.append(str(item.property_2))
        if item.property_3:
            p_3.append(str(item.property_3))
        if item.property_4:
            p_4.append(str(item.property_4))
        if str(products[0].maincategory.slug) == 'notebooks' or str(products[0].maincategory.slug) =='komplektuyushie':
            if item.property_5:
                p_5.append(str(item.property_5))
        if str(products[0].maincategory.slug) == 'notebooks':
            if item.property_6:
                p_6.append(str(item.property_6))
    p1d = Counter(p_1)
    p1b = p1d.items
    p2d = Counter(p_2)
    p2b = p2d.items
    p3d = Counter(p_3)
    p3b = p3d.items
    p4d = Counter(p_4)
    p4b = p4d.items
    p5d = Counter(p_5)
    p5b = p5d.items
    p6d = Counter(p_6)
    p6b = p6d.items
    if request.method == 'POST':
        tri_1 = request.POST.getlist('item1')
        tri_2 = request.POST.getlist('item2')
        tri_3 = request.POST.getlist('item3')
        tri_4 = request.POST.getlist('item4')
        tri_5 = request.POST.getlist('item5')
        tri_6 = request.POST.getlist('item6')
        tri_price = request.POST.getlist('price')
        tri_kol = request.POST.getlist('kolvo_check')
        if tri_1:
            products = products.filter(property_1__in = tri_1)
        if tri_2:
            products = products.filter(property_2__in=tri_2)
        if tri_3:
            products = products.filter(property_3__in=tri_3)
        if tri_4:
            products = products.filter(property_4__in=tri_4)
        if tri_5:
            products = products.filter(property_5__in=tri_5)
        if tri_6:
            products = products.filter(property_6__in=tri_6)
        if tri_price:
            stroka = str(tri_price[0])
            stroka = stroka.replace('UZS','')
            stroka = stroka.replace(' ', '')
            stroka = stroka.split('-')
            curs = get_object_or_404(Utility,name='dollar')
            curs=curs.value
            min=float(stroka[0])/float(curs)
            max=float(stroka[1])/float(curs)
            products = products.exclude(price__lt=int(min)).exclude(price__gt=int(max))
        if tri_kol:
            if tri_kol[0] == 'True':
                products = products.exclude(stock=0)

# КОНЕЦ БЛОКА ФОРМЫ ФИЛЬТРАЦИИ !!!!!>
    form=ChoisListForm(request.GET)
    shablon='list.html'
    if form.is_valid():
        cd = form.cleaned_data
        if cd['chos'] == True:
            shablon = 'list2.html'
        else:
            shablon = 'list.html'




    return render(request,shablon, {
        'category': Category_notebook,
        'products': products,
        'title': title,
        'cart_product_form': cart_product_form,
        'p1': p1b,
        'p2': p2b,
        'p3': p3b,
        'p4': p4b,
        'p5': p5b,
        'p6': p6b,
        'min_price':min_price,
        'max_price':max_price,
        'prop_list':prop_list
        #'form':form
    })



def ProductDetail(request, big_category_slug, category_slug, slug):
    big_category_slug = str(big_category_slug)
    cart_product_form = CartAddProductForm()
    related = {}
    if big_category_slug == 'notebooks':
        hub = get_object_or_404(HubNotebook, id=slug)
        products = Notebook.objects.filter(hub=slug)
        product=products[0]
        related = Notebook.objects.filter(
            Q(
                property_2 = product.property_2
            ) | Q(
                property_3 = product.property_3
            ) | Q(
                property_4 = product.property_4
            ) | Q(
                property_5 = product.property_5
            ) | Q(
                property_6 = product.property_6
            )

        )
        for prod in products:
            related = related.exclude(name=prod.name)
    elif big_category_slug == 'komplektuyushie':
        hub = get_object_or_404(HubComplecting, id=slug)
        products = Complecting.objects.filter(hub=slug)
        product = products[0]
        related = Complecting.objects.filter(
            Q(
                property_2=product.property_2
            ) | Q(
                property_3=product.property_3
            ) | Q(
                property_4=product.property_4
            ) | Q(
                property_5=product.property_5
            )
        )
        for prod in products:
            related = related.exclude(name=prod.name)
    elif big_category_slug == 'acses':
        hub = get_object_or_404(HubAcses, id=slug)
        products = Acses.objects.filter(hub=slug)
        product = products[0]
        related = Acses.objects.filter(
            Q(
                property_2=product.property_2
            ) | Q(
                property_3=product.property_3
            ) | Q(
                property_4=product.property_4
            )
        )
        for prod in products:
            related = related.exclude(name=prod.name)
    elif big_category_slug == 'perf':
        hub = get_object_or_404(HubPerf, id=slug)
        products = Perf.objects.filter(hub=slug)
        product = products[0]
        related = Perf.objects.filter(
            Q(
                property_2=product.property_2
            ) | Q(
                property_3=product.property_3
            ) | Q(
                property_4=product.property_4
            )
        )
        for prod in products:
            related = related.exclude(name=prod.name)
    elif big_category_slug == 'kompyutery':
        hub = get_object_or_404(HubPC, id=slug)
        products = PC.objects.filter(hub=slug)
        product = products[0]
        related = Complecting.objects.filter(
            Q(
                property_2=product.property_2
            ) | Q(
                property_3=product.property_3
            ) | Q(
                property_4=product.property_4
            ) | Q(
                property_5=product.property_5
            ) | Q(
                property_1=product.property_1
            )
        )
    title = str(products[0].hub.name)+' - PCShop.uz'

    obj, created = ProductStat.objects.get_or_create(
        defaults={
            "product_slug": product.slug,
            "product_cat": big_category_slug,
            "date": timezone.now()
            },
        date=timezone.now(), product_slug=slug, product_cat=big_category_slug
    )
    comments = Reviews.objects.filter(product=hub.slug, category=product.maincategory.slug)
    prop_list = product.category.prop_list
    prop_list = prop_list.split(', ')
    obj.views += 1
    obj.save(update_fields=['views'])
    checker = 0
    if request.method == 'POST':
        if request.recaptcha_is_valid:
            f = ReviewsForm(request.POST)
            f = f.save(commit=False)
            f.product= hub.slug
            f.category = hub.maincategory.slug
            f.ocenka = f.ocenka*20
            f.save()
    return render(request, 'product.html', {
        'products': products,
        'title': title,
        'cart_product_form': cart_product_form,
        'prop_list':prop_list,
        'hub':hub,
        'related': related,
        'checker':checker,
        'form':ReviewsForm,
        'coments':comments
    })

def main(request):
    notebooks = Notebook.objects.values('name','property_1','property_2','property_3','property_4','property_5','property_6','image','price','available','created','category','maincategory','slug')
    perfs = Perf.objects.values('name', 'image', 'price', 'property_1','property_2','property_3','property_4', 'available', 'created','category','maincategory','slug')
    acses = Acses.objects.values('name', 'property_1','property_2','property_3','property_4', 'image', 'price',  'available', 'created','category','maincategory','slug')
    complectings = Complecting.objects.values('name', 'property_1','property_2','property_3','property_4','property_5','image', 'price', 'available', 'created','category','maincategory','slug')
    pcs = PC.objects.values('name', 'property_1', 'property_2', 'property_3', 'property_4', 'property_5',
                                        'property_6', 'image', 'price', 'available', 'created', 'category',
                                        'maincategory', 'slug')

    allnews = list(notebooks)+list(perfs)+list(acses)+list(complectings)+list(pcs)
    allnews.sort(key=lambda x: x['created'])
    allnews.reverse()
    allnews = allnews[:6]
    link_n=list()
    for newin in allnews:
        if newin['maincategory']==2:
            var_n = get_object_or_404(Complecting, slug=newin['slug'])
            var_b = var_n.get_absolute_url
            link_n.append(var_b)
        elif newin['maincategory']==1:
            var_n = get_object_or_404(Notebook, slug=newin['slug'])
            var_b = var_n.get_absolute_url
            link_n.append(var_b)
        elif newin['maincategory']==3:
            var_n = get_object_or_404(Perf, slug=newin['slug'])
            var_b = var_n.get_absolute_url
            link_n.append(var_b)
        elif newin['maincategory']==4:
            var_n = get_object_or_404(Acses, slug=newin['slug'])
            var_b = var_n.get_absolute_url
            link_n.append(var_b)


    popular = ProductStat.objects.filter(date__range=[timezone.now() - timezone.timedelta(7), timezone.now()]).values('product_slug', 'product_cat').annotate(views=Sum('views')).order_by('-views')[:6]
    link_c=list()
    pop_c=list()
    for popular_c in popular:
        if popular_c['product_cat'] == 'notebooks':
            product_c = Notebook.objects.filter(slug=popular_c['product_slug']).values('name','property_1','property_2','property_3','property_4','property_5','property_6','image','price','available','created','category','maincategory','slug')
            pop_c += list(product_c)
            var_c = get_object_or_404(Notebook, slug=popular_c['product_slug'])
            var_b = var_c.get_absolute_url
            link_c.append(var_b)
        elif popular_c['product_cat'] == 'komplektuyushie':
            product_c = Complecting.objects.filter(slug=popular_c['product_slug']).values('name', 'property_1','property_2','property_3','property_4','property_5','image', 'price', 'available', 'created','category','maincategory','slug')
            pop_c += list(product_c)
            var_c = get_object_or_404(Complecting, slug=popular_c['product_slug'])
            var_b = var_c.get_absolute_url
            link_c.append(var_b)
        elif popular_c['product_cat'] == 'acses':
            product_c = Acses.objects.filter(slug=popular_c['product_slug']).values('name', 'property_1','property_2','property_3','property_4', 'image', 'price',  'available', 'created','category','maincategory','slug')
            pop_c +=list(product_c)
            var_c = get_object_or_404(Acses, slug=popular_c['product_slug'])
            var_b = var_c.get_absolute_url
            link_c.append(var_b)
        elif popular_c['product_cat'] == 'perf':
            product_c = Perf.objects.filter(slug=popular_c['product_slug']).values('name', 'property_1','property_2','property_3','property_4', 'image', 'price',  'available', 'created','category','maincategory','slug')
            pop_c += product_c
            var_c = get_object_or_404(Perf, slug=popular_c['product_slug'])
            var_b = var_c.get_absolute_url
            link_c.append(var_b)
        if popular_c['product_cat'] == 'kompyutery':
            product_c = PC.objects.filter(slug=popular_c['product_slug']).values('name','property_1','property_2','property_3','property_4','property_5','property_6','image','price','available','created','category','maincategory','slug')
            pop_c += list(product_c)
            var_c = get_object_or_404(PC, slug=popular_c['product_slug'])
            var_b = var_c.get_absolute_url
            link_c.append(var_b)

    shake=list()
    shakers=ShakeProduct.objects.all()
    for shaker in shakers:
        if shaker.maincategory.slug=='notebooks':
            var_s=get_object_or_404(Notebook,slug=shaker.name)
            shake.append(var_s)
        elif shaker.maincategory.slug=='komplektuyushie':
            var_s=get_object_or_404(Complecting,slug=shaker.name)
            shake.append(var_s)
        elif shaker.maincategory.slug=='perf':
            var_s=get_object_or_404(Perf,slug=shaker.name)
            shake.append(var_s)
        elif shaker.maincategory.slug=='acses':
            var_s=get_object_or_404(Acses,slug=shaker.name)
            shake.append(var_s)


    return render(request, 'index.html', {'title': 'PCShop.uz - Главная',
                                          'news': allnews,
                                          'pop_c': pop_c,
                                          'link_c': link_c,
                                          'link_n': link_n,
                                          'shake': shake})



def about_us(request):
    return render(request,'contacts.html',{'title':'О нас - PCshop.uz'})
     #obj, created = ProductStat.objects.get_or_create(
     #       defaults={
     #           "product": product,
     #           "date": timezone.now()
     #       },
     #       # При этом определяем, забор объекта статистики или его создание
     #       # по двум полям: дата и внешний ключ на статью
     #       date=timezone.now(), product=product
     #   )
     #   obj.views += 1  # инкрементируем счётчик просмотров и обновляем поле в базе данных
     #   obj.save(update_fields=['views'])
