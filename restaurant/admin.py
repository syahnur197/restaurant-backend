from django.contrib import admin

from .models import User, Restaurant, Branch, UserProfile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        # 'password',
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


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address', 'restaurant')
    list_filter = ('restaurant',)
    search_fields = ('name',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'role')
    list_filter = ('user',)