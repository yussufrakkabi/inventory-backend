## Overview of API Endpoints

## Authentication
- Login: POST /api/token/
{
    "username": "sktzzzz",
    "password": "0558218264"
}

## Categories:
- GET /api/categories/
- POST /api/categories/
- GET /api/categories/{id}/
- PUT /api/categories/{id}/
- DELETE /api/categories/{id}/
{
  "name": "Fruits",
  "description": "Fresh Greens"
}


## Products:
- GET /api/products/
- POST /api/products/
- GET /api/products/{id}/
- PUT /api/products/{id}/
- DELETE /api/products/{id}/
{
  "name": "Mango",
  "category": 1,
  "description": "Yellow Mangos",
  "quantity": "100",
  "price": "10"
}
http://127.0.0.1:8000/api/products/3/

## Suppliers:
- GET /api/suppliers/
- POST /api/suppliers/
- GET /api/suppliers/{id}/
- PUT /api/suppliers/{id}/
- DELETE /api/suppliers/{id}/
{
   "name": "Frank",
   "contact_email": "franklit@gmail.com",
   "phone_number": "0558218264",
   "contact_address": "Golf Main St" 
}


## Customers:
- GET /api/customers/
- POST /api/customers/
- GET /api/customers/{id}/
- PUT /api/customers/{id}/
- DELETE /api/customers/{id}/
{
    "name": "Fritz",
    "email": "fritzkiop@gmail.com",
    "phone_number": "85521",
    "contact_address": "Ridge"
}


## Orders:
- GET /api/orders/
- POST /api/orders/
- GET /api/orders/{id}/
- PUT /api/orders/{id}/
- DELETE /api/orders/{id}/
{
    "order_number": "1",
    "customer": 1,  
    "products": [1], 
    "status": "C",
    "total_price": "10.50"
}


## Inventories:
- GET /api/inventories/
- POST /api/inventories/
- GET /api/inventories/{id}/
- PUT /api/inventories/{id}/
- DELETE /api/inventories/{id}/
- Custom Action: GET /api/inventories/view_inventory_levels/
{
    "product": 1,
    "quantity": 50
}


## Inventory Logs:
- GET /api/inventory-logs/
- GET /api/inventory-logs/{id}/
{
    "product": "",
    "change_quantity": ""
}


### Nuggets
Check User Account Status:

Ensure that the user account you are trying to authenticate is active.
from django.contrib.auth.models import User
user = User.objects.filter(username='sktzzzz').first()
print(user.is_active)  # Should return True for an active account

If the user is not found or is not active, you may need to create the user or reactivate the account.
Creating a New User (if needed): If you don’t have an active user account, you can create one:

from django.contrib.auth.models import User
User.objects.create_user(username='sktzzzz', password='0558218264')

If you think you might have forgotten your password or want to set a new one for the existing user
user = User.objects.get(username='sktzzzz')
user.set_password('new_password')
user.save()

If you find that the user exists but is not active, you can activate it by setting is_active to True:
user.is_active = True
user.save()


http://127.0.0.1:8000/api/token/
{
    "username": "sktzzzz",
    "password": "0558218264"
}


Example Testing Scenario

Use the access token in your requests:

Send a GET request to /api/inventory/ to list inventories.

Send a POST request to /api/inventory/ to create a new inventory item.
{
  "product": 1,
  "quantity": 50
}

Send a PUT request to update an inventory item.
Send a DELETE request to remove an inventory item.


POST http://127.0.0.1:8000/api/token/refresh/
{
    "refresh": "your_refresh_token"
}
