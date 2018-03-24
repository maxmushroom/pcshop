# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 09:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20170905_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название')),
                ('value', models.CharField(db_index=True, max_length=200, verbose_name='Значение')),
            ],
        ),
        migrations.AlterField(
            model_name='productstat',
            name='date',
            field=models.DateField(default=datetime.datetime(2017, 10, 3, 9, 59, 54, 375138, tzinfo=utc), verbose_name='Дата'),
        ),
    ]
