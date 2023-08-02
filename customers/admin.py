from django.contrib import admin
from customers.models import Customer, Gem, Deal


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'spent_money']
    ordering = ['id']


@admin.register(Gem)
class GemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']


@admin.register(Deal)
class DealAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'gem', 'money', 'quantity', 'date']
    ordering = ['id']
