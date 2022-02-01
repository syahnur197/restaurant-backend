from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from restaurant.models import User, UserProfile
from subscriptions.models import UserSubscription

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    UserProfile.objects.create(user=user, role=UserProfile.Role.ACCOUNT_OWNER)

@receiver(user_signed_up)
def create_user_subscription(request, user, **kwargs):
    UserSubscription.objects.create(user=user, package=UserSubscription.Package.FREE)
