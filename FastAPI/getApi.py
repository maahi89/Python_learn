# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/")
# def home():
#     return "FastAPI is working"

from fastapi import FastAPI
app=FastAPI()
@app.get("/")
def home():
    return "First fastapi application is working"

@app.get("/user/{id}")
def get_user(id: int):
    return f"User id is {id}"

@app.get("/mahi")
def home():
    return "First fastapi application is working"

