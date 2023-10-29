from django.core.validators import MinValueValidator
from django.db import models
from django.db.models import Sum


class Product(models.Model):
    customer = models.CharField(max_length=100, null=False, blank=False, verbose_name='логин покупателя')
    item = models.CharField(max_length=100, null=False, blank=False, verbose_name='Наименование товара')
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма заказа", validators=(MinValueValidator(0),))
    quantity = models.PositiveIntegerField(verbose_name='Количество товара')
    date = models.DateTimeField(verbose_name='дата и время регистрации заказа')
