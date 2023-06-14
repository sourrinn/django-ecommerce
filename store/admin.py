from django.contrib import admin
from .models import Product, Order, OrderItem, Customer


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock']
    list_editable = ['price', 'stock']
    list_filter = ['category']
    search_fields = ['name', 'category']


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'total_price', 'order_date']
    list_filter = ['order_date']
    search_fields = ['id', 'customer__username']
    inlines = [OrderItemInline]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'email']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(Customer, CustomerAdmin)
