from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSubscription(models.Model):

    TRIAL_DURATION_DAYS = 30

    class Package(models.TextChoices):
        FREE = 'free-package', _('Free')
        LOW = 'low-package', _('Basic')
        MID = 'mid-package', _('Silver')
        HIGH = 'high-package', _('Gold')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_subscription')
    package = models.CharField(max_length=20, choices=Package.choices, default=Package.FREE)
    trial_starts_at = models.DateField("Trial Start Date", blank=True, null=True)
    trial_ends_at = models.DateField("Trial End Date", blank=True, null=True)
    subscription_starts_at = models.DateField("Subscription Start Date", blank=True, null=True)
    subscription_ends_at = models.DateField("Subscription End Date", blank=True, null=True)

