from django.contrib import admin

from store.models import Category, Order, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'inventory', 'unit_price']
    list_per_page = 10
    list_editable = ['unit_price']

