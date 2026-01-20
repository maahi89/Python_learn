from fastapi import FastAPI, HTTPException
app=FastAPI()
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
