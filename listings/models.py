from django.urls import reverse
from django.db import models
from realtors.models import Realtor


class Listing(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    is_published = models.BooleanField(
        default=True, verbose_name='وضعیت انتشار'
    )
    state = models.CharField(max_length=50, verbose_name='استان')
    city = models.CharField(max_length=50, verbose_name='شهر')
    address = models.CharField(max_length=255, verbose_name='آدرس')
    zipcode = models.CharField(max_length=50, verbose_name='کدپستی')
    descriptions = models.TextField(blank=True, verbose_name='توضیحات')
    price = models.IntegerField(default='On Agreement', verbose_name='قیمت')
    bedrooms = models.IntegerField(verbose_name='تعداد اتاق خواب')
    bathrooms = models.DecimalField(
        max_digits=2, decimal_places=1, verbose_name='تعداد حمام و دستشویی'
    )
    garage = models.IntegerField(default=0, verbose_name='تعداد پارکینگ')
    square_meters = models.IntegerField(verbose_name='مساحت')
    lot_size = models.DecimalField(
        max_digits=5, decimal_places=1, verbose_name='اندازه زمین'
    )
    listed_date = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ ایجاد'
    )
    realtor = models.ForeignKey(
        to=Realtor, on_delete=models.SET_NULL, null=True, verbose_name='مشاور املاک'
    )
    main_photo = models.ImageField(
        upload_to='photos/%Y/%m/%d', verbose_name='تصویر اصلی'
    )
    photo_1 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۱'
    )
    photo_2 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۲'
    )
    photo_3 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۳'
    )
    photo_4 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۴'
    )
    photo_5 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۵'
    )
    photo_6 = models.ImageField(
        upload_to='photos/%Y/%m/%d', blank=True, verbose_name='تصویر ۶'
    )

    class Meta:
        verbose_name = 'لیست شده‌ها'
        verbose_name_plural = 'لیست شده‌ها'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("listing", kwargs={"listing_id": self.pk})
