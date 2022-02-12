# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from .models import Image, User, CuisineType, MealType, DiningType, Restaurant, Branch, OpeningHour, UserProfile, Product, Order, OrderProduct, PaymentGateway, Payment

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


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
    )
    raw_id_fields = ('groups', 'user_permissions')


@admin.register(CuisineType)
class CuisineTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    search_fields = ('slug',)


@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    search_fields = ('slug',)


@admin.register(DiningType)
class DiningTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug')
    search_fields = ('slug',)


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'status',
        'activate_date',
        'deactivate_date',
        'approved_at',
        'rejected_at',
        'name',
        'description',
        'phone_number',
        'facebook',
        'instagram',
        'twitter',
        'website',
        'email',
        'creator',
        'origin_country',
    )
    list_filter = (
        'created',
        'modified',
        'activate_date',
        'deactivate_date',
        'approved_at',
        'rejected_at',
        'creator',
    )
    raw_id_fields = ('cuisine_types', 'dining_types', 'meal_types')
    search_fields = ('name',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'restaurant',
        'name',
        'payment_instruction',
        'phone_number',
        'address',
        'country',
        'latitude',
        'longitude',
    )
    list_filter = ('created', 'modified', 'restaurant')
    search_fields = ('name',)


@admin.register(OpeningHour)
class OpeningHourAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'branch',
        'days',
        'start_time',
        'end_time',
        'break_start_time',
        'break_end_time',
    )
    list_filter = ('created', 'modified', 'branch')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'restaurant',
        'branch',
        'role',
    )
    list_filter = ('created', 'modified', 'user', 'restaurant', 'branch')


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


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'user',
        'total_price',
        'note',
        'type',
        'payment_type',
        'status',
    )
    list_filter = ('created', 'modified', 'user')


@admin.register(OrderProduct)
class OrderProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'modified',
        'order',
        'quantity',
        'price',
    )
    list_filter = ('created', 'modified', 'order')


@admin.register(PaymentGateway)
class PaymentGatewayAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'restaurant',
        'branch',
        'merchant_id',
        'api_password',
    )
    list_filter = ('restaurant', 'branch')


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'status',
        'order',
        'session_id',
        'session_version',
        'success_indicator',
        'restaurant',
        'branch',
        'paid_at',
    )
    list_filter = ('order', 'restaurant', 'branch', 'paid_at')
