import email
from django.db import models


class Realtor(models.Model):
    name = models.CharField(max_length=200, verbose_name='نام')
    descriptions = models.TextField(blank=True, verbose_name='توضیحات')
    phone = models.CharField(max_length=30, verbose_name='شماره تلفن')
    email = models.EmailField(verbose_name='پست الکترونیکی')
    is_mvp = models.BooleanField(default=False, verbose_name='فرشنده برتر ماه')
    hire_date = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ استخدام'
    )
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d', verbose_name='تصویر'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'مشاورین املاک'
        verbose_name_plural = 'مشاورین املاک'
