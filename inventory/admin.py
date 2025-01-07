from django.contrib import admin
from .models import Category, Product, Supplier, Inventory, InventoryLog, Customer, Order


# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)
    list_filter = ('name',)

# Product Admin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'date_added', 'last_updated')
    search_fields = ('name', 'category__name')
    list_filter = ('category', 'price')
    ordering = ('-date_added',)

# Supplier Admin
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_email', 'phone_number', 'contact_address')
    search_fields = ('name', 'contact_email')
    list_filter = ('name',)

# Inventory Admin
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'last_updated')
    search_fields = ('product__name',)
    list_filter = ('product',)
    ordering = ('-last_updated',)

# Inventory Log Admin
@admin.register(InventoryLog)
class InventoryLogAdmin(admin.ModelAdmin):
    list_display = ('product', 'change_quantity', 'timestamp')  
    search_fields = ('product__name',)
    list_filter = ('timestamp',)  
    ordering = ('-timestamp',)

# Customer Admin
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')  # Use 'full_name' instead of 'first_name' and 'last_name'
    search_fields = ('name', 'email')
    list_filter = ('email',)


# Order Admin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer', 'status', 'total_price') 
    search_fields = ('order_number', 'customer__first_name', 'customer__last_name')
    list_filter = ('status',)
