from django.db import models
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField



class Tuning(models.Model):
    class Meta:
        verbose_name = 'Настройки сайта'
        verbose_name_plural = 'Настройки сайта'

    robots = models.TextField('robots.txt', null=True, blank=True)
    script = models.TextField('Скрипты', null=True, blank=True)

    def __str__(self):
        return self.robots


class Blog(models.Model):
    class Meta:
        verbose_name = 'Наполнение сайта'
        verbose_name_plural = 'Наполнение сайта'

    title = models.CharField('Название товара', max_length=250)
    description = models.TextField('Описание товара', null=True, blank=True)
    photo = models.ImageField('Фото', upload_to='event_photo', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Bid(models.Model):
    class Meta:
        verbose_name = 'Описание заказа'
        verbose_name_plural = 'Описание заказа'

    cat = models.ForeignKey(Blog, on_delete=models.PROTECT, verbose_name='Товар')
    surname = models.CharField('Фамилия', max_length=250, null=True, blank=True)
    name = models.CharField('Имя', max_length=250, null=True, blank=True)
    patronymic = models.CharField('Отчество', max_length=250, null=True, blank=True)
    phoneNumber = PhoneNumberField(unique=True, null=True, blank=True)
    email = models.EmailField(label='Email')
    country = CountryField(blank=True)
    city = models.CharField('Отчество', max_length=250, null=True, blank=True)
    color = models.CharField('Цвет', max_length=250, null=True, blank=True)
    size = models.IntegerField('Размер', null=True, blank=True)
    quantity = models.IntegerField('Количество', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.color
