from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Image,  Product

"""
To register generics
"""


class ImageInline(GenericStackedInline):
    model = Image

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'content_type',
        'object_id',
        'image',
    )
    list_filter = ('created', 'modified', 'content_type')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'status',
        'activate_date',
        'deactivate_date',
        'name',
        'description',
        'restaurant',
        'unit_price',
        'discount_price',
    )
    list_filter = (
        'created',
        'modified',
        'activate_date',
        'deactivate_date',
        'restaurant',
    )
    search_fields = ('name',)
    inlines = [
        ImageInline,
    ]
