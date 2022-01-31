from allauth.account.signals import user_signed_up
from django.dispatch import receiver

from restaurant.models import User, UserProfile

@receiver(user_signed_up)
def create_user_profile(request, user, **kwargs):
    UserProfile.objects.create(user=user)
