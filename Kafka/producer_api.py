from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from kafka import KafkaProducer

app = FastAPI()

templates = Jinja2Templates(
    directory="templates"
)

producer = KafkaProducer(
    bootstrap_servers='localhost:9092'
)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

@app.post("/order")
def order_food(food: str = Form(...)):

    producer.send(
        'food_orders',
        food.encode('utf-8')
    )

    producer.flush()

    return {
        "message": f"{food} order sent!"
    }