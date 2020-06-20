from django.contrib import admin
from .models import Item, OrderItem, Cart, BillingAddress, Category, Payment

admin.site.register(Item)
admin.site.register(Category)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(BillingAddress)
admin.site.register(Payment)
