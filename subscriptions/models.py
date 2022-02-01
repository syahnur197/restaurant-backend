from django.db import models
from django_extensions.db.models import TitleSlugDescriptionModel
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class Package(TitleSlugDescriptionModel, models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.title

class UserSubscription(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_subscription')
    package = models.ForeignKey(Package, on_delete=models.PROTECT)
    trial_starts_at = models.DateField("Trial Start Date", blank=True, null=True)
    trial_ends_at = models.DateField("Trial End Date", blank=True, null=True)
    subscription_starts_at = models.DateField("Subscription Start Date", blank=True, null=True)
    subscription_ends_at = models.DateField("Subscription End Date", blank=True, null=True)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='subscription_order')
    user_subscription = models.ForeignKey(UserSubscription, on_delete=models.SET_NULL, null=True, blank=True)
