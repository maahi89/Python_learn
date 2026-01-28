from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app=FastAPI()
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


# Database
users_db = []
products_db = []
users_login = {
    "admin": "password123",
    "user1": "pass456"
}

users = {
    1: {"id": 1, "name": "Mahitha", "age": 25, "city": "Delhi"},
    2: {"id": 2, "name": "Admin", "age": 30, "city": "Mumbai"},
    3: {"id": 3, "name": "User1", "age": 28, "city": "Bangalore"},
    4: {"id": 4, "name": "User2", "age": 22, "city": "Pune"},
}

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 30000},
    {"id": 3, "name": "Tablet", "price": 20000},
]

@app.get("/")
def home():
    return {"message": "GET example FastAPI"}

@app.get("/user/{id}")
def get_user(id:int):
    if id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[id]

@app.get("/users")
def all_users():
    return {list(users.values())}

@app.get("/search")
def search_user(name:str):
    for user in users.values():
        if user["name"].lower()==name.lower():
            return user
        else:
            raise HTTPException(status_code=404, detail="User not found")
        
@app.get("/filter")
def filter_users(age: int , city: str = None):
    result=list(users.values())
    if age:
        result=[u for u in result if u["age"]==age]
    if city:
        result=[u for u in result if u["city"].lower()==city.lower()]
    return {"results": result}  


@app.post("/users")
def create_user(user:User):
    """Create a new user"""
    new_user={"id":len(users_db)+1, **user.dict()}
    users_db.append(new_user)
    return{"message":"user created", "user":new_user}

@app.post("/users/validate")
def create_user_validate(user:User):
    """Create  user with validation"""
    if user.age<18:
        raise HTTPException(status_code=400, detail="User must be 18 or older")
    if "@" not in user.email:
        raise HTTPException(status_code=400, detail="Invalid email format")
    new_user={"id":len(users_db)+1, **user.dict()}
    users_db.append(new_user)       
    return{"message":"User created successfully", "user":new_user}

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
    

@app.put("/users/{user_id}")
def update_user(user_id: int, user_update: UpdateUserRequest):
    """update user details"""
    if user_id not in users:
        raise HTTPException(status_code=404, details="user not found")
    user=users_db[user_id]
    if user_update.name is not None:
        user["name"]=user_update.name
    if user_update.email is not None:
        user["email"]=user_update.email
    if user_update.age is not None:
        user["age"]=user_update.age
    return {"message": "User updated successfully", "user": user}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    """delete the user"""
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    delete_user=users.pop(user_id)
    return {"message": "deleted successsfully", "user":delete_user}

@app.delete("/users")
def delete_all_users(confirm: bool = False):
    """delete all users with confirmation"""
    if not  confirm:
        raise HTTPException(status_code=400, detail="Confirmation required to delete all users")
    users.clear()
    return{"message": "All users deleted successfully", "total_users": len(users)}

@app.delete("/product/by_name/{product_name}")
def delete_product_by_name(product_name:str):
    """delete product by name"""
    for product_id, product in list(products_db.items()):
        if product["name"].lower()==product_name.lower():
            deleted_product=products_db.pop(product_id)
            return{"message":"Product deleted successfully", "product":deleted_product}