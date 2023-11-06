from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, verbose_name='نام')
    email = models.EmailField(verbose_name='پست الکترونیکی')
    phone = models.CharField(max_length=30, verbose_name='شماره تلفن')
    message = models.TextField(blank=True, verbose_name='متن پیام')
    listing = models.CharField(max_length=200, verbose_name='عنوان آگهی')
    listing_id = models.IntegerField(verbose_name='شناسه آگهی')
    user_id = models.IntegerField(blank=True, verbose_name='شناسه کاربر')
    contact_date = models.DateTimeField(
        auto_now_add=True, verbose_name='تاریخ تماس'
    )

    class Meta:
        verbose_name = 'تماس‌ها'
        verbose_name_plural = 'تماس‌ها'

    def __str__(self):
        return self.name
