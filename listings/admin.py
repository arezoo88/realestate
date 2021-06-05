from django.contrib import admin
from .models import Listing, Photo


class PhotoInline(admin.TabularInline):
    model = Photo
    extra = 3


class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['realtor', 'title', 'address', 'city', 'state', 'zipcode', 'description', 'price',
                           'bedrooms', 'bathrooms', 'garage', 'sqft', 'lot_size', 'photo_main', 'is_published']}),

        ('Date Information', {'fields': ['list_date'], 'classes': ['collapse']})

    ]
    list_display = ('title','realtor','city','price')
    list_filter = ('title','realtor')
    inlines = [PhotoInline]


# admin.site.register(Question)
# admin.site.register(Choice)
admin.site.register(Listing, ListingAdmin)
