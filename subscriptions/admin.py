# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Package, UserSubscription, Order


@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'slug', 'price')
    search_fields = ('slug',)


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'package',
        'trial_starts_at',
        'trial_ends_at',
        'subscription_starts_at',
        'subscription_ends_at',
    )
    list_filter = (
        'user',
        'trial_starts_at',
        'trial_ends_at',
        'subscription_starts_at',
        'subscription_ends_at',
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'user_subscription')
    list_filter = ('user', 'user_subscription')
