from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Pydantic Models
class User(BaseModel):
    name: str
    email: str
    age: int

class Product(BaseModel):
    name: str
    price: float
    quantity: int

class LoginRequest(BaseModel):
    username: str
    password: str

class Address(BaseModel):
    street: str
    city: str
    country: str

class FullUser(BaseModel):
    name: str
    email: str
    address: Address

# Database
users_db = []
products_db = []
users_login = {
    "admin": "password123",
    "user1": "pass456"
}

# 1. Simple POST - Create User
@app.post("/users")
def create_user(user: User):
    """Create a new user"""
    new_user = {"id": len(users_db) + 1, **user.dict()}
    users_db.append(new_user)
    return {"message": "User created", "user": new_user}

# 2. POST with Validation
@app.post("/users/validate")
def create_user_validate(user: User):
    """Create user with validation"""
    if user.age < 18:
        raise HTTPException(status_code=400, detail="User must be 18 or older")
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    
    new_user = {"id": len(users_db) + 1, **user.dict()}
    users_db.append(new_user)
    return {"message": "User created successfully", "user": new_user}

# 3. POST Product
@app.post("/products")
def create_product(product: Product):
    """Create a new product"""
    new_product = {"id": len(products_db) + 1, **product.dict()}
    products_db.append(new_product)
    return {"message": "Product created", "product": new_product}

# 4. POST Login
@app.post("/login")
def login(request: LoginRequest):
    """User login"""
    if request.username not in users_login:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    if users_login[request.username] != request.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    return {
        "message": f"Welcome {request.username}",
        "token": f"fake-jwt-token-{request.username}",
        "username": request.username
    }

# 5. POST with Multiple Items (List)
@app.post("/bulk-users")
def create_bulk_users(users_list: List[User]):
    """Create multiple users at once"""
    created_users = []
    for user in users_list:
        new_user = {"id": len(users_db) + 1, **user.dict()}
        users_db.append(new_user)
        created_users.append(new_user)
    
    return {
        "message": f"{len(created_users)} users created",
        "users": created_users
    }

# 6. POST with Nested Model
@app.post("/users/full")
def create_full_user(full_user: FullUser):
    """Create user with nested address"""
    new_user = {
        "id": len(users_db) + 1,
        "name": full_user.name,
        "email": full_user.email,
        "address": full_user.address.dict()
    }
    users_db.append(new_user)
    return {"message": "User with address created", "user": new_user}

# 7. POST with Optional Fields
@app.post("/products/discount")
def create_product_discount(
    product: Product,
    discount: float = 0
):
    """Create product with optional discount"""
    final_price = product.price * (1 - discount / 100)
    new_product = {
        "id": len(products_db) + 1,
        **product.dict(),
        "discount": discount,
        "final_price": final_price
    }
    products_db.append(new_product)
    return {"message": "Product created with discount", "product": new_product}

# 8. POST with Calculation
@app.post("/calculate")
def calculate(num1: float, num2: float):
    """Calculate sum, difference, multiply, divide"""
    return {
        "sum": num1 + num2,
        "difference": num1 - num2,
        "multiply": num1 * num2,
        "divide": num1 / num2 if num2 != 0 else "Cannot divide by zero"
    }

# 9. POST Order
class OrderItem(BaseModel):
    product_id: int
    quantity: int

@app.post("/orders")
def create_order(items: List[OrderItem]):
    """Create order with multiple items"""
    total_quantity = sum(item.quantity for item in items)
    return {
        "order_id": 101,
        "items": items,
        "total_items": total_quantity,
        "status": "Order placed successfully"
    }

# 10. POST with Status Response
@app.post("/feedback")
def submit_feedback(message: str, rating: int):
    """Submit feedback with rating"""
    if rating < 1 or rating > 5:
        raise HTTPException(status_code=400, detail="Rating must be between 1 and 5")
    
    return {
        "feedback_id": 1001,
        "message": message,
        "rating": rating,
        "status": "Feedback received",
        "thank_you": "Thank you for your feedback!"
    }
