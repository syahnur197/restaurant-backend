import imp
from operator import mod
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    pass

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    branches = models.ManyToOneRel

    def __str__(self):
        return self.name
    
class Branch(models.Model):
    class Meta:
        verbose_name_plural = "branches"

    name = models.CharField(max_length=100)
    address = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class UserProfile(models.Model):
    
    class Role(models.TextChoices):
        RESTAURANT_ADMIN = 'restaurant-admin', _('Restaurant Admin')
        RESTAURANT_MANAGER = 'restaurant-manager', _('Restaurant Manager')
        RESTAURANT_FINANCE = 'restaurant-finance', _('Restaurant Finance')
        BRANCH_MANAGER = 'branch-manager', _('Branch Manager')
        BRANCH_STAFF = 'branch-staff', _('Branch Staff')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.RESTAURANT_ADMIN
    )