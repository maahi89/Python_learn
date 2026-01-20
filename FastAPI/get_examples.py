from fastapi import FastAPI, HTTPException

app = FastAPI()

# Sample data
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

# 1. Simple GET - Home endpoint
@app.get("/")
def home():
    return {"message": "GET Examples API"}

# 2. GET with Path Parameter
@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]

# 3. GET All Users
@app.get("/users")
def get_all_users():
    return {"users": list(users.values())}

# 4. GET with Query Parameter
@app.get("/search")
def search_user(name: str):
    for user in users.values():
        if user["name"].lower() == name.lower():
            return user
    raise HTTPException(status_code=404, detail="User not found")

# 5. GET with Multiple Query Parameters
@app.get("/filter")
def filter_users(age: int = None, city: str = None):
    result = list(users.values())
    
    if age:
        result = [u for u in result if u["age"] == age]
    if city:
        result = [u for u in result if u["city"].lower() == city.lower()]
    
    return {"results": result}

# 6. GET All Products
@app.get("/products")
def get_products():
    return {"products": products, "total": len(products)}

# 7. GET Product by ID
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    raise HTTPException(status_code=404, detail="Product not found")

# 8. GET with Optional Query Parameter (default value)
@app.get("/products/price")
def get_by_price(min_price: int = 0, max_price: int = 100000):
    result = [p for p in products if min_price <= p["price"] <= max_price]
    return {"products": result}

# 9. GET User Count
@app.get("/count/users")
def count_users():
    return {"total_users": len(users)}

# 10. GET Statistics
@app.get("/stats")
def get_stats():
    return {
        "total_users": len(users),
        "total_products": len(products),
        "average_user_age": sum(u["age"] for u in users.values()) / len(users),
        "average_product_price": sum(p["price"] for p in products) / len(products)
    }
