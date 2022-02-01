# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import UserSubscription


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
