from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel

class User(AbstractUser):
    pass

class Cuisine(TitleSlugDescriptionModel):
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Restaurant(TimeStampedModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    cuisines = models.ManyToManyField(Cuisine)

    def __str__(self):
        return self.name
    
    
class Branch(TimeStampedModel, models.Model):
    class Meta:
        verbose_name_plural = "branches"

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    payment_instruction = models.TextField()
    
    def __str__(self):
        return self.name

class UserProfile(TimeStampedModel, models.Model):
    
    class Role(models.TextChoices):
        RESTAURANT_ADMIN = 'restaurant-admin', _('Restaurant Admin')
        RESTAURANT_MANAGER = 'restaurant-manager', _('Restaurant Manager')
        RESTAURANT_FINANCE = 'restaurant-finance', _('Restaurant Finance')
        BRANCH_MANAGER = 'branch-manager', _('Branch Manager')
        BRANCH_STAFF = 'branch-staff', _('Branch Staff')
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True) # set null if restaurant is deleted
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True) # set null if branch is deleted
    full_name = models.CharField(max_length=100)
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.RESTAURANT_ADMIN
    )
    
class Product(TimeStampedModel, ActivatorModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    
class Order(TimeStampedModel, models.Model):
    
    class OrderType(models.TextChoices):
        PICK_UP = 'pick-up', _('Pick Up')
        DELIVERY = 'delivery', _('Delivery')
        DINE_IN = 'dine-in', _('Dine In')
        
    class PaymentType(models.TextChoices):
        BANK_TRANSFER = 'bank-transfer', _('Bank Transfer')
        ONLINE_PAYMENT = 'online-payment', _('Online Payment')
        CASH_ON_DELIVERY = 'cash-on-delivery', _('Cash on Delivery')
        CASH_ON_COUNTER = 'cash-on-counter', _('Cash on Counter')
    
    class Status(models.TextChoices):
        PENDING = 'pending', _('Pending Payment')
        PAID = 'paid', _('Paid')
        PREPARING = 'preparing', _('Preparing')
        READY = 'ready', _('Ready')
        COMPLETED = 'completed', _('Completed')
        DELIVERED = 'delivered', _('Delivered')
        CANCEL = 'cancel', _('Cancel')
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL)
    total_price = models.DecimalField(max_digits=7, decimal_places=2)
    note = models.TextField()
    type = models.CharField(
        max_length=20,
        choices=OrderType.choices,
        default=OrderType.DELIVERY
    )
    payment_type = models.CharField(
        max_length=30,
        choices=PaymentType.choices,
        default=PaymentType.BANK_TRANSFER
    )
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING
    )

class OrderProduct(TimeStampedModel, models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)