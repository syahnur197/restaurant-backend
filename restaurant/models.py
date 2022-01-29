from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from django_countries.fields import CountryField

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
    facebook = models.CharField(max_length=50, blank=True, null=True)
    instagram = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    origin_country = CountryField(default="BN")

    def __str__(self):
        return self.name
    
    
class Branch(TimeStampedModel, models.Model):
    class Meta:
        verbose_name_plural = "branches"

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    payment_instruction = models.TextField()
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    country = CountryField(default="BN")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    
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
    
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
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

class PaymentGateway(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    merchant_id = models.CharField(max_length=30)
    api_password = models.CharField(max_length=100)

class Payment(models.Model):

    class Status(models.TextChoices):
        PENDING_PAYMENT = 'pending-payment', _('Pending Payment')
        PAYMENT_RECEIVED = 'payment-received', _('Payment Received')
        ON_HOLD = 'on-hold', _('On Hold')
        COMPLETED = 'completed', _('Completed')
        CANCELLED = 'cancelled', _('Cancelled')
        REFUNDED = 'refunded', _('Refunded')
        FAILED = 'failed', _('Failed')

    status = models.CharField(
        max_length=30,
        choices=Status.choices,
        default=Status.PENDING_PAYMENT
    )
    session_id = models.CharField(max_length=100)
    session_version = models.CharField(max_length=30)
    success_indicator = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    paid_at = models.DateTimeField(null=True)

