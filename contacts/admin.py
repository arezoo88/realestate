from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'email','listing')
    search_fields = ('name', 'email', 'listing')
    list_per_page = 10


admin.site.register(Contact,ContactAdmin)
