from django.contrib import admin
from .models import Product, ProductImage, Category

class ProductImageInline(admin.TabularInline):  
    model = ProductImage  
    extra = 1

class ProductAdmin(admin.ModelAdmin):  
    list_display = ('name', 'price', 'category', 'stock', 'created_at')  
    inlines = [ProductImageInline]  

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
