### API Design Blueprint

#### **Authentication**
- **Login Endpoint**
  - **Path**: `POST /api/token/`
  - **Description**: Generates an access token and refresh token for user authentication.
  - **Request Body**:
    ```json
    {
        "username": "admin",
        "password": "admin"
    }
    ```
  - **Response**:
    ```json
    {
        "access": "access_token",
        "refresh": "refresh_token"
    }
    ```

- **Refresh Token**
  - **Path**: `POST /api/token/refresh/`
  - **Description**: Refreshes the access token using the refresh token.
  - **Request Body**:
    ```json
    {
        "refresh": "your_refresh_token"
    }
    ```
  - **Response**:
    ```json
    {
        "access": "new_access_token"
    }
    ```

---

#### **Categories**
- **Endpoints**:
  - `GET /api/categories/`: Retrieve all categories.
  - `POST /api/categories/`: Create a new category.
  - `GET /api/categories/{id}/`: Retrieve details of a specific category.
  - `PUT /api/categories/{id}/`: Update a category.
  - `DELETE /api/categories/{id}/`: Delete a category.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "name": "Fruits",
      "description": "Fresh Greens"
  }
  ```

---

#### **Products**
- **Endpoints**:
  - `GET /api/products/`: Retrieve all products.
  - `POST /api/products/`: Add a new product.
  - `GET /api/products/{id}/`: Retrieve details of a specific product.
  - `PUT /api/products/{id}/`: Update a product.
  - `DELETE /api/products/{id}/`: Delete a product.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "name": "Mango",
      "category": 1,
      "description": "Yellow Mangos",
      "quantity": 100,
      "price": 10
  }
  ```

---

#### **Suppliers**
- **Endpoints**:
  - `GET /api/suppliers/`: Retrieve all suppliers.
  - `POST /api/suppliers/`: Add a new supplier.
  - `GET /api/suppliers/{id}/`: Retrieve details of a specific supplier.
  - `PUT /api/suppliers/{id}/`: Update a supplier.
  - `DELETE /api/suppliers/{id}/`: Delete a supplier.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "name": "Frank",
      "contact_email": "franklit@gmail.com",
      "phone_number": "0558218264",
      "contact_address": "Golf Main St"
  }
  ```

---

#### **Customers**
- **Endpoints**:
  - `GET /api/customers/`: Retrieve all customers.
  - `POST /api/customers/`: Add a new customer.
  - `GET /api/customers/{id}/`: Retrieve details of a specific customer.
  - `PUT /api/customers/{id}/`: Update a customer.
  - `DELETE /api/customers/{id}/`: Delete a customer.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "name": "Fritz",
      "email": "fritzkiop@gmail.com",
      "phone_number": "85521",
      "contact_address": "Ridge"
  }
  ```

---

#### **Orders**
- **Endpoints**:
  - `GET /api/orders/`: Retrieve all orders.
  - `POST /api/orders/`: Create a new order.
  - `GET /api/orders/{id}/`: Retrieve details of a specific order.
  - `PUT /api/orders/{id}/`: Update an order.
  - `DELETE /api/orders/{id}/`: Delete an order.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "order_number": "1",
      "customer": 1,
      "products": [1],
      "status": "C",
      "total_price": 10.50
  }
  ```

---

#### **Inventories**
- **Endpoints**:
  - `GET /api/inventories/`: Retrieve all inventory items.
  - `POST /api/inventories/`: Add a new inventory item.
  - `GET /api/inventories/{id}/`: Retrieve details of a specific inventory item.
  - `PUT /api/inventories/{id}/`: Update an inventory item.
  - `DELETE /api/inventories/{id}/`: Delete an inventory item.
  - **Custom Action**: `GET /api/inventories/view_inventory_levels/`: View inventory levels.

- **Example Request Body** (for POST/PUT):
  ```json
  {
      "product": 1,
      "quantity": 50
  }
  ```

---

#### **Inventory Logs**
- **Endpoints**:
  - `GET /api/inventory-logs/`: Retrieve all inventory logs.
  - `GET /api/inventory-logs/{id}/`: Retrieve a specific inventory log.

- **Example Response Body**:
  ```json
  {
      "product": "Mango",
      "change_quantity": 20
  }
  ```

---

