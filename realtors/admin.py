from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'email', 'hire_date'
    list_display_links = 'id', 'name'
    list_per_page = 20
    search_fields = 'name',


admin.site.register(Realtor, RealtorAdmin)
