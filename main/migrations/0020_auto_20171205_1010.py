# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-05 10:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20171124_1137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200, verbose_name='Ваше имя')),
                ('review', models.TextField(verbose_name='Ваше отзыв')),
                ('category', models.CharField(max_length=200)),
                ('product', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ocenka', models.IntegerField(verbose_name='Оценка')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.AlterField(
            model_name='productstat',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 12, 5, 10, 10, 54, 597338, tzinfo=utc), verbose_name='Дата'),
        ),
    ]