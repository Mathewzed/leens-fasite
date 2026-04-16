from django.contrib import admin
from .models import Product, Collection, ContactMessage, Order, ProductRating, Newsletter

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    ordering = ['-created_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'collection']
    list_filter = ['collection']
    search_fields = ['name', 'description']
    list_editable = ['price', 'collection']
    ordering = ['-id']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    ordering = ['-created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'customer_name', 'phone', 'location', 'created_at', 'is_processed']
    list_filter = ['is_processed', 'created_at']
    search_fields = ['customer_name', 'phone', 'location', 'product__name']
    ordering = ['-created_at']

@admin.register(ProductRating)
class ProductRatingAdmin(admin.ModelAdmin):
    list_display = ['product', 'is_like', 'created_at']
    list_filter = ['is_like', 'created_at']
    search_fields = ['product__name']
    ordering = ['-created_at']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'subscribed_at']
    search_fields = ['email']
    ordering = ['-subscribed_at']