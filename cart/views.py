from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Notebook, Complecting, Acses, Perf, PC, PCForm
from .cart import Cart, Versus, Craft
from .forms import CartAddProductForm
from decimal import Decimal


@require_POST
def CartAdd(request, big_category_slug, slug):
    cart = Cart(request)
    if big_category_slug == 'notebooks':
        product = get_object_or_404(Notebook, slug=slug, available=True)
    elif big_category_slug == 'komplektuyushie':
        product = get_object_or_404(Complecting, slug=slug, available=True)
    elif big_category_slug == 'acses':
        product = get_object_or_404(Acses, slug=slug, available=True)
    elif big_category_slug == 'perf':
        product = get_object_or_404(Perf, slug=slug, available=True)
    elif big_category_slug == 'kompyutery':
        product = get_object_or_404(PC, slug=slug, available=True)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart:CartDetail')


def CartRemove(request, product_slug):
    cart = Cart(request)
    cart.remove(product_slug)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    title = 'Корзина - PCShop.uz'
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={
                'quantity': item['quantity'],
                'update': True
            })

    for popular_c in cart:
        if popular_c['big_cat'] == 'notebooks':
            var_c = get_object_or_404(Notebook, slug=popular_c['slug'])
            cart.cart[popular_c['slug']]['product'] = var_c
        elif popular_c['big_cat'] == 'komplektuyushie':
            var_c = get_object_or_404(Complecting, slug=popular_c['slug'])
            cart.cart[popular_c['slug']]['product'] = var_c
        elif popular_c['big_cat'] == 'acses':
            var_c = get_object_or_404(Acses, slug=popular_c['slug'])
            cart.cart[popular_c['slug']]['product'] = var_c
        elif popular_c['big_cat'] == 'perf':
            var_c = get_object_or_404(Perf, slug=popular_c['slug'])
            cart.cart[popular_c['slug']]['product'] = var_c
        elif popular_c['big_cat'] == 'kompyutery':
            var_c = get_object_or_404(PC, slug=popular_c['slug'])
            cart.cart[popular_c['slug']]['product'] = var_c

    for item in cart.cart.values():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']

    total_price = int(cart.get_total_price())

    return render(request, '../../main/templates/cart.html', {'cart_t': cart,
                                                              'vs': cart.cart,
                                                              'title': title,
                                                              'total_price': total_price,
                                                              'test': cart})


def VersusAdd(request, big_category_slug, slug):
    versus = Versus(request)
    versus.versus_add(product=slug, big_category_slug=big_category_slug)
    return redirect('cart:VersusDetail')


def VersusRemove(request, product_slug):
    versus = Versus(request)
    versus.remove(product_slug)
    return redirect('cart:VersusDetail')


def VersusDetail(request):
    versus = Versus(request)
    var_v = list()
    link_v = list()
    vs = list()
    for popular_c in versus:
        if 'category' in popular_c:
           if popular_c['category'] == 'notebooks':
               product_c = Notebook.objects.filter(slug= popular_c['name'])
               var_v += list(product_c)
               var_c = get_object_or_404(Notebook, slug= popular_c['name'])
               var_b = var_c.get_absolute_url
               link_v.append(var_b)
           elif popular_c['category'] == 'komplektuyushie':
               product_c = Complecting.objects.filter(slug= popular_c['name'])
               var_v += list(product_c)
               var_c = get_object_or_404(Complecting, slug= popular_c['name'])
               var_b = var_c.get_absolute_url
               link_v.append(var_b)
           elif popular_c['category'] == 'acses':
               product_c = Acses.objects.filter(slug= popular_c['name'])
               var_v +=list(product_c)
               var_c = get_object_or_404(Acses, slug= popular_c['name'])
               var_b = var_c.get_absolute_url
               link_v.append(var_b)
           elif popular_c['category'] == 'perf':
               product_c = Perf.objects.filter(slug= popular_c['name'])
               var_v += product_c
               var_c = get_object_or_404(Perf, slug= popular_c['name'])
               var_b = var_c.get_absolute_url
               link_v.append(var_b)
           elif popular_c['category'] == 'kompyutery':
               product_c = PC.objects.filter(slug= popular_c['name'])
               var_v += product_c
               var_c = get_object_or_404(PC, slug= popular_c['name'])
               var_b = var_c.get_absolute_url
               link_v.append(var_b)
           if var_v[0].category.prop_list != '':
                vs = var_v[0].category.prop_list.split(',')
    title = 'Сравнение - PCShop.uz'




    return render(request, '../../main/templates/versus.html', {'versus': var_v,
                                                                'vs':vs,
                                                                 'title' :title} )


def CraftAdd(request, big_category_slug, category_slug, slug):
    craft = Craft(request)
    craft.craft_add(product=slug, big_category_slug=big_category_slug, category_slug=category_slug)
    return redirect('cart:CraftDetail')


def CraftRemove(request, big_category_slug, product_slug):
    craft = Craft(request)
    craft.remove(big_category_slug, product_slug)
    return redirect('cart:CraftDetail')


def CraftDetail(request):
    craft = Craft(request)
    form = PCForm
    detail1 = ''
    detail2 = ''
    detail3 = ''
    detail4 = ''
    detail5 = ''
    detail6 = ''
    detail7 = ''
    detail8 = ''
    detail9 = ''
    price = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    error_ram = ''
    error_cpu = ''
    cpu_socket = ''
    motherboard_socket = ''
    ram_ddr = ''
    motherboard_ddr = ''
    checker = ''

    if request.POST:
        if request.POST['property_1'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_1'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'cpu' in craft.craft:
            craft.remove('komplektuyishie', 'proc')

        if request.POST['property_2'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_2'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'ram' in craft.craft:
            craft.remove('komplektuyishie', 'ram')

        if request.POST['property_3'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_3'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'video' in craft.craft:
            craft.remove('komplektuyishie', 'video')

        if request.POST['property_4'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_4'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'hdd' in craft.craft:
            craft.remove('komplektuyishie', 'hdd')

        if request.POST['property_5'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_5'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'motherboard' in craft.craft:
            craft.remove('komplektuyishie', 'matb')

        if request.POST['property_6'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_6'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'bp_1' in craft.craft:
            craft.remove('komplektuyishie', 'bp_1')

        if request.POST['property_7'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_7'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'bp_2' in craft.craft:
            craft.remove('komplektuyishie', 'bp_2')

        if request.POST['property_8'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_8'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'coolers' in craft.craft:
            craft.remove('komplektuyishie', 'cool')

        if request.POST['property_9'] != '':
            item=get_object_or_404(Complecting,pk=request.POST['property_9'])
            craft.craft_add(product=item.slug, big_category_slug=item.maincategory.slug, category_slug=item.category.slug)
        elif 'dvd' in craft.craft:
            craft.remove('komplektuyishie', 'dvd')


    if 'cpu' in craft.craft:
        detail1 = get_object_or_404(Complecting, slug=craft.craft['cpu']['name'])
        price[0]=(detail1.price)
        cpu_socket=detail1.property_2
    if 'ram' in craft.craft:
        detail2 = get_object_or_404(Complecting, slug=craft.craft['ram']['name'])
        price[1] =(detail2.price)
        ram_ddr = detail2.property_1[:4]
    if 'video' in craft.craft:
        detail3 = get_object_or_404(Complecting, slug=craft.craft['video']['name'])
        price[2] =(detail3.price)
    if 'hdd' in craft.craft:
        detail4 = get_object_or_404(Complecting, slug=craft.craft['hdd']['name'])
        price[3] =(detail4.price)
    if 'motherboard' in craft.craft:
        detail5 = get_object_or_404(Complecting, slug=craft.craft['motherboard']['name'])
        price[4] =(detail5.price)
        motherboard_socket=detail5.property_2
        motherboard_ddr=detail5.property_4[:4]
    if 'bp_1' in craft.craft:
        detail6 = get_object_or_404(Complecting, slug=craft.craft['bp_1']['name'])
        price[5] =(detail6.price)
    if 'bp_2' in craft.craft:
        detail7 = get_object_or_404(Complecting, slug=craft.craft['bp_2']['name'])
        price[6] =(detail7.price)
    if 'coolers' in craft.craft:
        detail8 = get_object_or_404(Complecting, slug=craft.craft['coolers']['name'])
        price[7] =(detail8.price)
    if 'dvd' in craft.craft:
        detail9 = get_object_or_404(Complecting, slug=craft.craft['dvd']['name'])
        price[8] =(detail9.price)
    detail_perf = {}
    detail_acses = {}

    if 'perf' in craft.craft:
        for perfer in craft.craft['perf']:
            detail_perf[perfer]=get_object_or_404(Perf, slug=perfer)

    if 'acses' in craft.craft:
        for acsesor in craft.craft['acses']:
            detail_acses[acsesor] = get_object_or_404(Acses, slug=acsesor)

    form = form(initial={
        'property_1': detail1,
        'property_2': detail2,
        'property_3': detail3,
        'property_4': detail4,
        'property_5': detail5,
        'property_6': detail6,
        'property_7': detail7,
        'property_8': detail8,
        'property_9': detail9
    })

    if (cpu_socket != motherboard_socket) or (cpu_socket == ''):
        error_cpu='Данный процессор не совместим с выбранной материнской платой! '+motherboard_socket+' и '+cpu_socket
    if (ram_ddr != motherboard_ddr) or (ram_ddr == ''):
        error_ram= 'Выбранная оперативная память '+ram_ddr+' не подходит к данной материнской плате!'
    title = 'Сборка - PCShop.uz'

    return render(request, '../../main/templates/craft.html', {'form': form,
                                                                'title': title,
                                                               'detail_perf': detail_perf,
                                                               'detail_acses': detail_acses,
                                                               'price': price,
                                                               'error_cpu':error_cpu,
                                                               'error_ram':error_ram,
                                                               'checker':checker})

