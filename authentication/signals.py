from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from restaurant.models import User, UserProfile
from subscriptions.models import Package, UserSubscription

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    UserProfile.objects.create(user=user, role=UserProfile.Role.ACCOUNT_OWNER)

@receiver(user_signed_up)
def create_user_subscription(request, user, **kwargs):
    # Assume first package is free package
    free_package = Package.objects.first()
    UserSubscription.objects.create(user=user, package=free_package)
