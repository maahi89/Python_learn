from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for login request
class LoginRequest(BaseModel):
    username: str
    password: str

# Sample user database (in production, use a real database)
users = {
    "admin": "password123",
    "user1": "pass456",
    "mahit": "secret789"
}

@app.get("/")
def home():
    return {"message": "FastAPI Login Application"}

@app.post("/login")
def login(request: LoginRequest):
    """Login endpoint - checks username and password"""
    
    # Check if username exists
    if request.username not in users:
        raise HTTPException(status_code=401, detail="Invalid username")
    
    # Check if password matches
    if users[request.username] != request.password:
        raise HTTPException(status_code=401, detail="Invalid password")
    
    # Login successful
    return {
        "message": f"User {request.username} logged in successfully",
        "username": request.username,
        "status": "success"
    }

@app.post("/register")
def register(request: LoginRequest):
    """Register a new user"""
    if request.username in users:
        raise HTTPException(status_code=400, detail="Username already exists")
    
    users[request.username] = request.password
    return {"message": f"User {request.username} registered successfully"}