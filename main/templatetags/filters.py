
#! coding: utf-8
from django import template
from main.models import Utility
from django.shortcuts import render, render_to_response, get_object_or_404
#
register = template.Library()
curs = get_object_or_404(Utility, name='dollar')
curs = int(curs.value)
#
@register.filter
def price_convert(value, seperator=u' '):
    if value != '':
        value=int(value)
        if isinstance(value, float):
            value = value*curs
        if isinstance(value, int):
            value = value*curs
        value = str(value)
        penny = ' '
    # Если целая часть меньше 3-х символов -
    # то ее разделять не нужно
        if len(value) <= 3:
            return value + penny
        parts = []
    # Выбираем по три символа в список
        while value:
            parts.append(value[-3:])
            value = value[:-3]
    # Сортируем список в обратном порядке
        parts.reverse()
    # Возвращаем результат
        return seperator.join(parts) + penny
    else:
        return 0

@register.filter
def price_convert_dos(value, seperator=u' '):
    value=int(value)
    if isinstance(value, float):
        value = value*curs+30000
    if isinstance(value, int):
        value = value*curs+30000
    value = str(value)
    penny = ' '
    # Если целая часть меньше 3-х символов -
    # то ее разделять не нужно
    if len(value) <= 3:
        return value + penny
    parts = []
    # Выбираем по три символа в список
    while value:
        parts.append(value[-3:])
        value = value[:-3]
    # Сортируем список в обратном порядке
    parts.reverse()
    # Возвращаем результат
    return seperator.join(parts) + penny

@register.filter
def price_convert_int(value, seperator=u' '):
    if value != '':
        value=int(value)
        if isinstance(value, float):
            value = value*curs
        if isinstance(value, int):
            value = value*curs
        return value
    else:
        return 0


@register.filter
def vers_prop(product,number):
    if number==1:
        return product.property_1
    elif number==2:
        return product.property_2
    elif number==3:
        return product.property_3
    elif number==4:
        return product.property_4
    elif number==5:
        return product.property_5
    elif number==6:
        return product.property_6
    elif number==7:
        return product.property_7
    elif number==8:
        return product.property_8
    elif number==9:
        return product.property_9
