from django.contrib import admin
from .models import *
# Register your models here.

class ProductImageAdmin(admin.StackedInline):
    model = ProductImage

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted', 'discounted_price', 'category', 'product_image', 'is_inStock']
    list_filter = ['discounted', 'category', 'is_inStock']
    # list_editable = ['discounted', 'is_inStock']
    list_per_page = 5
    search_fields = ("id", "title",)
    inlines = [ProductImageAdmin]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'contact', 'locality', 'city', 'zipcode', 'state']
    list_filter = ['user']
    search_fields = ("id", "user")

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'title', 'quantity']

@admin.register(OrderPlaced)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer', 'product', 'quantity', 'title', 'discounted', 'price', 'ordered_date', 'status']
    list_filter = ['user', 'ordered_date', 'status', 'discounted']

@admin.register(DailyAwareness)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'image','video']

