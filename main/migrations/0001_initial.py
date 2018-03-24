# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название категории', max_length=255)),
                ('alias', models.SlugField(verbose_name='Alias категории')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(verbose_name='Название товара', max_length=255)),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('image', models.CharField(verbose_name='Ссылка на картинку', max_length=255)),
                ('alias', models.SlugField(verbose_name='Alias товара')),
                ('category', models.ForeignKey(to='main.Category')),
            ],
        ),
    ]
