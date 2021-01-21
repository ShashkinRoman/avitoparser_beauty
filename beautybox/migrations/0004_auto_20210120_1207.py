# Generated by Django 3.1.5 on 2021-01-20 12:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautybox', '0003_auto_20210120_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='url',
            name='region_name',
        ),
        migrations.AddField(
            model_name='url',
            name='search_request',
            field=models.CharField(max_length=255, null=True, verbose_name='Поисковый запрос'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='address',
            field=models.CharField(max_length=1000, null=True, verbose_name='Адрес'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='contact_name',
            field=models.CharField(max_length=255, null=True, verbose_name='Контактное лицо'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created',
            field=models.CharField(max_length=255, null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Дата парсинга информации'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='description',
            field=models.CharField(max_length=5000, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='owner_info',
            field=models.CharField(max_length=1000, null=True, verbose_name='Информация о владельце'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='phone',
            field=models.CharField(max_length=255, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='price',
            field=models.IntegerField(null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='title',
            field=models.CharField(max_length=1000, null=True, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='ad',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beautybox.url', verbose_name='Ссылка и запрос'),
        ),
        migrations.AlterField(
            model_name='url',
            name='url',
            field=models.CharField(max_length=1000, null=True, verbose_name='Ссылка'),
        ),
    ]
