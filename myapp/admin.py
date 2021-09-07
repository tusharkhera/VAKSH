from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted', 'discounted_price', 'description', 'category', 'product_image', 'is_inStock']

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'contact', 'locality', 'city', 'zipcode', 'state']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'title', 'quantity']

@admin.register(OrderPlaced)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'title', 'discounted', 'price', 'ordered_date', 'status']

@admin.register(DailyAwareness)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'image','video']