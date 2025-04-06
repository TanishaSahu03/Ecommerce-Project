from django.db import models
from django.contrib.auth.models import AbstractUser

class BaseUser(AbstractUser):

    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)    
    
    @property
    def user_type(self):
        if hasattr(self, 'vendor'):
            return "vendor"
        elif hasattr(self, 'customer'):
            return "customer"
        return "base"
    
    def __str__(self):
        return f"{self.username}"

class Customer(BaseUser):
    
    def __str__(self):
        return f"{self.id} {self.first_name}"

class Vendor(BaseUser):
    store_name = models.CharField(max_length=255, unique=True)
    business_license = models.FileField(upload_to='business_licenses/', blank=True, null=True)
    bank_account_number = models.CharField(max_length=20, unique=True)
    tax_id = models.CharField(max_length=20, unique=True)
    is_verified = models.BooleanField(default=True)

    def __str__(self):
        return self.store_name
