from django.contrib import admin
from .models import Customer, Vendor
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    
class VenderAdmin(admin.ModelAdmin):
    model = Vendor
    
admin.site.register(Vendor,VenderAdmin)
admin.site.register(Customer,CustomerAdmin)