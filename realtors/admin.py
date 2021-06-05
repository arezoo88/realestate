from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'is_mvp')
    list_display_links = ('id', 'name')
    list_filter = ('name', 'email')
    list_editable = ('is_mvp',)
    search_fields = ('name', 'email', 'phone')
    list_per_page = 2

admin.site.register(Realtor, RealtorAdmin)
