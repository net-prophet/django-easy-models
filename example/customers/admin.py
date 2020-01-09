from django.contrib import admin
from .models import Customer
from example.purchases.models import Purchase

class PurchaseInLine(admin.TabularInline):
    model = Purchase


class CustomerAdmin(admin.ModelAdmin):
    model = Customer
    list_display = ('full_name', 'state', 'gender', 'age')
    list_filter = ('full_name', 'state', 'gender', 'age')
    inlines = [PurchaseInLine]

admin.site.register(Customer, CustomerAdmin)
