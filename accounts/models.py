from django.db import models

from django.contrib.auth.models import AbstractBaseUser

from .managers import UserManager


class User(AbstractBaseUser):

    # USER = 1
    # PROPERTYOWNER = 2

    # ROLE_CHOICE = (
    #     (USER, 'User'),
    #     (PROPERTYOWNER, 'Property Owner'),
    # )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username= models.CharField(max_length = 45,unique=True)
    email = models.CharField(max_length=50,unique=True)
    phone_number = models.CharField(max_length=13,blank=True)
    # role = models.PositiveSmallIntegerField(choices =ROLE_CHOICE, blank = True,null = True )

    is_customer = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = UserManager()
    
    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roomsStayed = models.IntegerField(default=0)

class Seller(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    roomCount = models.IntegerField(default=0)
    rating = models.FloatField(default=5)

'''
from accounts.models import Customer, Seller, User
c=User.create_user(email='', username = '', password='')
c.save()
c.is_seller() = True
c.save()
customer_c = Customer.objects.create(user=c,roomsStayed=6)
seller_c = Seller.objects.create(user=c,roomsCount=16, rating =4.5)
'''

