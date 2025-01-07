from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser



# Category Model
class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


# Product Model
class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Supplier Model
class Supplier(models.Model):
    name = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    contact_address = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# Inventory Model
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"
    

# Inventory Log Model
class InventoryLog(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    change_quantity = models.IntegerField()  # Positive for restock, negative for sales
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Customer Model
class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    contact_address = models.CharField(max_length=255)

    def __str__(self):
        return self.name


# Order Model
class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('R', 'Refunded'),
        ('S', 'Shipped'),
    ]

    order_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    status = models.CharField(max_length=1, choices=ORDER_STATUS_CHOICES, default='P')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Order {self.order_number} - {self.customer.name}"