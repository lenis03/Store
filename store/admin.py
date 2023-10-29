from django.contrib import admin

from store.models import Category, Order, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'inventory', 'unit_price', 'inventory_status']
    list_per_page = 10
    list_editable = ['unit_price']

    def inventory_status(self, product: Product):
        if product.inventory < 10:
            return 'Low'
        elif product.inventory > 50:
            return 'Hight'
        return 'Medium'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'status', 'datetime_created']
    list_per_page = 10
    list_editable = ['status']
    ordering = ['-datetime_created']


admin.site.register(Category)