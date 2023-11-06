from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'price', 'listed_date', 'realtor'
    list_display_links = 'id', 'title'
    list_filter = 'realtor', 'is_published'
    list_editable = 'is_published',
    list_per_page = 20
    search_fields = 'title', 'descriptions', 'address', 'city', 'state', 'zipcode', 'price'


admin.site.register(Listing, ListingAdmin)
