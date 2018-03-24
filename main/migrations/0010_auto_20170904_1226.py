# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-04 12:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20170904_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productstat',
            name='product',
        ),
        migrations.AddField(
            model_name='productstat',
            name='product_cat',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Откуда?'),
        ),
        migrations.AddField(
            model_name='productstat',
            name='product_slug',
            field=models.CharField(db_index=True, max_length=200, null=True, verbose_name='Что?'),
        ),
        migrations.AlterField(
            model_name='productstat',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 9, 4, 12, 26, 43, 671011, tzinfo=utc), verbose_name='Дата'),
        ),
    ]