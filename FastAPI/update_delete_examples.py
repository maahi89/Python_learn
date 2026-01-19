from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic Models
class UpdateUserRequest(BaseModel):
    name: str = None
    email: str = None
    age: int = None

class UpdateProductRequest(BaseModel):
    name: str = None
    price: float = None
    quantity: int = None

class UpdatePasswordRequest(BaseModel):
    username: str
    old_password: str
    new_password: str

# Sample Data
users_db = {
    1: {"id": 1, "name": "Mahit", "email": "mahit@example.com", "age": 25},
    2: {"id": 2, "name": "Admin", "email": "admin@example.com", "age": 30},
    3: {"id": 3, "name": "User1", "email": "user1@example.com", "age": 28},
}

products_db = {
    1: {"id": 1, "name": "Laptop", "price": 50000, "quantity": 5},
    2: {"id": 2, "name": "Mobile", "price": 30000, "quantity": 10},
    3: {"id": 3, "name": "Tablet", "price": 20000, "quantity": 8},
}

user_passwords = {
    "admin": "password123",
    "user1": "pass456",
    "mahit": "secret789"
}

# ============= PUT/UPDATE EXAMPLES =============

# 1. Simple PUT - Update User
@app.put("/users/{user_id}")
def update_user(user_id: int, user_data: UpdateUserRequest):
    """Update user information"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    user = users_db[user_id]
    if user_data.name:
        user["name"] = user_data.name
    if user_data.email:
        user["email"] = user_data.email
    if user_data.age:
        user["age"] = user_data.age
    
    return {"message": "User updated", "user": user}

# 2. PUT - Update Product
@app.put("/products/{product_id}")
def update_product(product_id: int, product_data: UpdateProductRequest):
    """Update product information"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    product = products_db[product_id]
    if product_data.name:
        product["name"] = product_data.name
    if product_data.price:
        product["price"] = product_data.price
    if product_data.quantity:
        product["quantity"] = product_data.quantity
    
    return {"message": "Product updated", "product": product}

# 3. PUT - Update Password
@app.put("/change-password")
def change_password(request: UpdatePasswordRequest):
    """Change user password"""
    if request.username not in user_passwords:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user_passwords[request.username] != request.old_password:
        raise HTTPException(status_code=401, detail="Old password is incorrect")
    
    user_passwords[request.username] = request.new_password
    return {"message": f"Password for {request.username} updated successfully"}

# 4. PUT - Update Product Price
@app.put("/products/{product_id}/price")
def update_product_price(product_id: int, new_price: float):
    """Update only product price"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    products_db[product_id]["price"] = new_price
    return {"message": "Price updated", "product": products_db[product_id]}

# 5. PUT - Update Product Quantity
@app.put("/products/{product_id}/quantity")
def update_product_quantity(product_id: int, quantity: int):
    """Update product quantity"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if quantity < 0:
        raise HTTPException(status_code=400, detail="Quantity cannot be negative")
    
    products_db[product_id]["quantity"] = quantity
    return {"message": "Quantity updated", "product": products_db[product_id]}

# 6. PUT - Bulk Update Users
@app.put("/users/bulk-update")
def bulk_update_users(updates: dict):
    """Update multiple users at once"""
    results = []
    for user_id, user_data in updates.items():
        user_id = int(user_id)
        if user_id in users_db:
            users_db[user_id].update(user_data)
            results.append(users_db[user_id])
    
    return {"message": f"{len(results)} users updated", "users": results}

# 7. PUT - Increment Product Quantity
@app.put("/products/{product_id}/increment")
def increment_quantity(product_id: int, amount: int = 1):
    """Increment product quantity"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    products_db[product_id]["quantity"] += amount
    return {"message": "Quantity incremented", "product": products_db[product_id]}

# 8. PUT - Apply Discount
@app.put("/products/{product_id}/discount")
def apply_discount(product_id: int, discount_percent: float):
    """Apply discount to product price"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if discount_percent < 0 or discount_percent > 100:
        raise HTTPException(status_code=400, detail="Discount must be between 0 and 100")
    
    original_price = products_db[product_id]["price"]
    discounted_price = original_price * (1 - discount_percent / 100)
    products_db[product_id]["discounted_price"] = discounted_price
    
    return {
        "message": "Discount applied",
        "original_price": original_price,
        "discount": f"{discount_percent}%",
        "final_price": discounted_price
    }

# 9. PUT - Activate/Deactivate User
@app.put("/users/{user_id}/status")
def toggle_user_status(user_id: int, active: bool):
    """Activate or deactivate user"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_id]["active"] = active
    status = "activated" if active else "deactivated"
    return {"message": f"User {status}", "user": users_db[user_id]}

# 10. PUT - Update User Role
@app.put("/users/{user_id}/role")
def update_user_role(user_id: int, role: str):
    """Update user role (admin, user, moderator)"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    valid_roles = ["admin", "user", "moderator"]
    if role not in valid_roles:
        raise HTTPException(status_code=400, detail=f"Role must be one of {valid_roles}")
    
    users_db[user_id]["role"] = role
    return {"message": "User role updated", "user": users_db[user_id]}

# ============= DELETE EXAMPLES =============

# 1. Simple DELETE - Delete User by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """Delete a user"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    deleted_user = users_db.pop(user_id)
    return {"message": "User deleted successfully", "deleted_user": deleted_user}

# 2. DELETE - Delete Product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    """Delete a product"""
    if product_id not in products_db:
        raise HTTPException(status_code=404, detail="Product not found")
    
    deleted_product = products_db.pop(product_id)
    return {"message": "Product deleted successfully", "deleted_product": deleted_product}

# 3. DELETE - Delete All Users
@app.delete("/users")
def delete_all_users(confirm: bool = False):
    """Delete all users (requires confirmation)"""
    if not confirm:
        raise HTTPException(status_code=400, detail="Add ?confirm=true to confirm deletion")
    
    count = len(users_db)
    users_db.clear()
    return {"message": f"{count} users deleted successfully"}

# 4. DELETE - Delete All Products
@app.delete("/products")
def delete_all_products(confirm: bool = False):
    """Delete all products (requires confirmation)"""
    if not confirm:
        raise HTTPException(status_code=400, detail="Add ?confirm=true to confirm deletion")
    
    count = len(products_db)
    products_db.clear()
    return {"message": f"{count} products deleted successfully"}

# 5. DELETE - Delete Product by Name
@app.delete("/products/by-name/{product_name}")
def delete_product_by_name(product_name: str):
    """Delete product by name"""
    for product_id, product in list(products_db.items()):
        if product["name"].lower() == product_name.lower():
            deleted = products_db.pop(product_id)
            return {"message": "Product deleted", "deleted_product": deleted}
    
    raise HTTPException(status_code=404, detail="Product not found")

# 6. DELETE - Remove User by Username
@app.delete("/users/by-name/{username}")
def delete_user_by_name(username: str):
    """Delete user by name"""
    for user_id, user in list(users_db.items()):
        if user["name"].lower() == username.lower():
            deleted = users_db.pop(user_id)
            if username in user_passwords:
                del user_passwords[username]
            return {"message": "User deleted", "deleted_user": deleted}
    
    raise HTTPException(status_code=404, detail="User not found")

# 7. DELETE - Clear Low Stock Products
@app.delete("/products/low-stock")
def delete_low_stock_products(threshold: int = 3):
    """Delete products with quantity below threshold"""
    to_delete = [pid for pid, p in products_db.items() if p["quantity"] < threshold]
    deleted_count = len(to_delete)
    
    for pid in to_delete:
        products_db.pop(pid)
    
    return {"message": f"{deleted_count} low stock products deleted"}

# 8. DELETE - Soft Delete (Archive User)
@app.delete("/users/{user_id}/archive")
def archive_user(user_id: int):
    """Archive user instead of deleting"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    users_db[user_id]["archived"] = True
    users_db[user_id]["active"] = False
    return {"message": "User archived", "user": users_db[user_id]}

# 9. DELETE - Delete Products by Price Range
@app.delete("/products/price-range")
def delete_by_price_range(min_price: float, max_price: float):
    """Delete products within price range"""
    to_delete = [pid for pid, p in products_db.items() if min_price <= p["price"] <= max_price]
    deleted_count = len(to_delete)
    
    for pid in to_delete:
        products_db.pop(pid)
    
    return {"message": f"{deleted_count} products deleted in price range {min_price}-{max_price}"}

# 10. DELETE - Delete User Account with Backup
@app.delete("/users/{user_id}/permanent")
def permanent_delete_user(user_id: int):
    """Permanently delete user account"""
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    
    backup = users_db.pop(user_id)
    username = backup.get("name")
    if username in user_passwords:
        del user_passwords[username]
    
    return {
        "message": "User account permanently deleted",
        "backup_data": backup,
        "note": "Backup data stored for recovery within 30 days"
    }
