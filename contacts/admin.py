from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = 'id', 'name', 'listing', 'contact_date'
    list_display_links = 'id', 'name'
    list_per_page = 20
    search_fields = 'name', 'email', 'listing'


admin.site.register(Contact, ContactAdmin)
