from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType

from django_extensions.db.models import ActivatorModel, TimeStampedModel, TitleSlugDescriptionModel
from django_countries.fields import CountryField

class ApprovableModel(models.Model):
    """
    ApprovabledModel

    An abstract base class model that provides the ability for admin to approve or reject the record
    """

    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_REJECTED = 'rejected'

    approved_at = models.DateTimeField('Approved At', blank=True, null=True)
    rejected_at = models.DateTimeField('Rejected At', blank=True, null=True)

    def get_approval_status(self):
        if self.approved_at is None and self.rejected_at is None:
            return self.STATUS_PENDING
        elif self.rejected_at is not None:
            return self.STATUS_REJECTED
        elif self.approved_at is not None:
            return self.STATUS_APPROVED

    class Meta:
        abstract = True

def get_upload_path(instance, filename):
    content_object = instance.content_object
    model = content_object.model.__class__._meta
    name = model.verbose_name_plural.replace(' ', '_')
    return f'restaurants/{name}/{content_object.id}/{filename}'
class Image(TimeStampedModel, models.Model):

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    image = models.ImageField(upload_to=get_upload_path, null=True, blank=True)




class User(AbstractUser):

    def has_user_profile(self):
        return hasattr(self, 'user_profile')

    def has_restaurant(self):
        user_profile = self.user_profile
        return user_profile.restaurant is not None

    def get_user_profile(self):
        return self.user_profile

    def get_user_restaurant(self):
        return self.get_user_profile().restaurant

    def get_user_branch(self):
        return self.get_user_profile().branch


class CuisineType(TitleSlugDescriptionModel):
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class MealType(TitleSlugDescriptionModel):
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class DiningType(TitleSlugDescriptionModel):
    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

class Restaurant(TimeStampedModel, ActivatorModel, ApprovableModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    phone_number = models.CharField(max_length=20)
    cuisine_types = models.ManyToManyField(CuisineType)
    dining_types = models.ManyToManyField(DiningType)
    meal_types = models.ManyToManyField(MealType)
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
    payment_instruction = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    country = CountryField(default="BN")
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_edit_link(self):
        return reverse_lazy('dashboard_branch_update', kwargs={'pk' : self.id})

    def get_opening_hours_link(self):
        return reverse_lazy('dashboard_opening_hour_list', kwargs={'pk' : self.id})

class OpeningHour(TimeStampedModel, models.Model):
    class Meta:
        verbose_name_plural = "Opening Hours"

    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    days = models.CharField('Days', max_length=100)
    start_time = models.TimeField('Opening Time')
    end_time = models.TimeField('Closing Time')
    break_start_time = models.TimeField('Break Time starts at', null=True, blank=True)
    break_end_time = models.TimeField('Break Time ends at', null=True, blank=True)

    def get_edit_link(self):
        return reverse_lazy('dashboard_opening_hour_update', kwargs={'pk' : self.branch.id, 'opening_hour_id' : self.id})

class UserProfile(TimeStampedModel, models.Model):

    class Role(models.TextChoices):
        ACCOUNT_OWNER = 'account-owner', _('Account Owner')
        RESTAURANT_ADMIN = 'restaurant-admin', _('Restaurant Admin')
        RESTAURANT_MANAGER = 'restaurant-manager', _('Restaurant Manager')
        RESTAURANT_FINANCE = 'restaurant-finance', _('Restaurant Finance')
        BRANCH_MANAGER = 'branch-manager', _('Branch Manager')
        BRANCH_STAFF = 'branch-staff', _('Branch Staff')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True) # set null if restaurant is deleted
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True) # set null if branch is deleted
    role = models.CharField(
        max_length=50,
        choices=Role.choices,
        default=Role.ACCOUNT_OWNER
    )

    def set_restaurant(self, restaurant):
        self.restaurant = restaurant
        return self.save()


"""
Place to upload images
"""
def product_photo_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/restaurant/<restaurant_id>/<filename>
    return 'restaurants/restaurant/{0}/{1}'.format(instance.restaurant.id, filename)

class Product(TimeStampedModel, ActivatorModel, models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    unit_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    discount_price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    image = models.ImageField(upload_to=product_photo_directory_path, null=True, blank=True)
    # images = GenericRelation(
    #     Image,
    #     content_type_field='content_type',
    #     object_id_field='object_id',
    # )

    def get_edit_link(self):
        return reverse_lazy('dashboard_product_update', kwargs={'pk' : self.id})

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
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    session_id = models.CharField(max_length=100)
    session_version = models.CharField(max_length=30)
    success_indicator = models.CharField(max_length=30)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, blank=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, null=True, blank=True)
    paid_at = models.DateTimeField(null=True)

