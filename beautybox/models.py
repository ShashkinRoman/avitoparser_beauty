from django.db import models
from datetime import datetime

category_parsing_dict = {
    "small": 1,
    "large": 2,
    "msk": 3,
    "mo": 4,
    'all': 5
}

parsing_status_dict = {
    "Parsing success": 1,
    "Not parsing": 2,
    "Failed first parsing": 3,
    "Failed parsing": 4,
    "Have note phone": 5,
}


class Region(models.Model):
    region_name = models.CharField(verbose_name="Город", max_length=255, null=True)
    region_name_in_url = models.CharField(verbose_name="Город в ссылке на авито", max_length=255, null=True)
    category_parsing = models.SmallIntegerField(verbose_name="Категория города по размеру",
                                                null=True, default=category_parsing_dict.get('all'))


class Url(models.Model):
    region = models.ForeignKey("Region", on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(verbose_name="Дата парсинга информации", default=datetime.now)
    url = models.CharField(verbose_name="Ссылка", max_length=1000, null=True, unique=True)
    search_request = models.CharField(verbose_name="Поисковый запрос", max_length=255, null=True)
    parsing_status = models.SmallIntegerField(verbose_name="Статус парсинга",
                                              default=parsing_status_dict.get('Not parsing'))


class Ad(models.Model):
    price = models.IntegerField(verbose_name="Цена", null=True)
    date = models.DateTimeField(verbose_name="Дата парсинга информации", default=datetime.now, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=1000, null=True)
    phone = models.CharField(verbose_name='Телефон', max_length=255, null=True)
    created = models.CharField(verbose_name="Дата создания", max_length=255, null=True)
    owner_info = models.CharField(verbose_name="Информация о владельце", max_length=1000, null=True)
    contact_name = models.CharField(verbose_name="Контактное лицо", max_length=255, null=True)
    address = models.CharField(verbose_name="Адрес", max_length=1000, null=True)
    description = models.CharField(verbose_name="Описание", max_length=5000, null=True)
    region = models.ForeignKey("Region", on_delete=models.CASCADE)
    url = models.ForeignKey("Url", verbose_name="Ссылка и запрос", on_delete=models.CASCADE)
