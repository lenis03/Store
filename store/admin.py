from django.contrib import admin
from django.http.request import HttpRequest
from django.db.models import Count

from store.models import Category, Comment, Order, Product


class InventoryFilter(admin.SimpleListFilter):
    LESS_THAN_3 = '3>'
    BETWEEN_3_AND_10 = '3<=10'
    MORE_THAN_10 = '10<'
    title = 'Critical Inventory Status'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            (InventoryFilter.LESS_THAN_3, 'High'),
            (InventoryFilter.BETWEEN_3_AND_10, 'Medium'),
            (InventoryFilter.MORE_THAN_10, 'OK')
        ]

    def queryset(self, request, queryset):
        if self.value() == InventoryFilter.LESS_THAN_3:
            return queryset.filter(inventory__lt=3)
        if self.value() == InventoryFilter.BETWEEN_3_AND_10:
            return queryset.filter(inventory__range=(3, 10))
        if self.value() == InventoryFilter.MORE_THAN_10:
            return queryset.filter(inventory__gt=10)


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
    list_filter = ['datetime_created', InventoryFilter]

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
