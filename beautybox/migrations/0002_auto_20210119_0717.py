# Generated by Django 3.1.5 on 2021-01-19 07:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beautybox', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата парсинга информации'),
        ),
        migrations.AlterField(
            model_name='region',
            name='category_parsing',
            field=models.SmallIntegerField(default=5, null=True, verbose_name='Категория города по размеру'),
        ),
        migrations.AlterField(
            model_name='url',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата парсинга информации'),
        ),
    ]
