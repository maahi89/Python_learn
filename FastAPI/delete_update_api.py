from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Pydantic model for update request
class UpdateRequest(BaseModel):
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
    return {"message": "FastAPI Delete and Update API"}

@app.put("/update-password")
def update_password(request: UpdateRequest):
    """Update user password"""
    
    # Check if username exists
    if request.username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update password
    users[request.username] = request.password
    return {"message": f"Password for {request.username} updated successfully"}

@app.delete("/delete-user/{username}")
def delete_user(username: str):
    """Delete a user"""
    
    # Check if username exists
    if username not in users:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Delete user
    del users[username]
    return {"message": f"User {username} deleted successfully"}

@app.get("/all-users")
def get_all_users():
    """Get all registered users (usernames only)"""
    return {"users": list(users.keys())}
