from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import Count

from store.models import Category, Comment, Order, Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'inventory',
        'unit_price',
        'inventory_status',
        'product_category'
        ]
    list_per_page = 10
    list_editable = ['unit_price']
    list_select_related = ['category']

    def inventory_status(self, product: Product):
        if product.inventory < 10:
            return 'Low'
        elif product.inventory > 50:
            return 'Hight'
        return 'Medium'

    @admin.display(ordering='category__title')
    def product_category(self, product: Product):
        return product.category.title


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'customer',
        'status',
        'datetime_created',
        'num_of_items'
        ]
    list_per_page = 10
    list_editable = ['status']
    ordering = ['-datetime_created']

    def get_queryset(self, request: HttpRequest):
        return super()\
                .get_queryset(request)\
                .prefetch_related('items') \
                .annotate(items_count=Count('items'))

    @admin.display(ordering='items_count')
    def num_of_items(self, order: Order):
        return order.items_count


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', 'datetime_created']
    list_per_page = 10
    list_editable = ['status']
    ordering = ['-datetime_created']


admin.site.register(Category)
