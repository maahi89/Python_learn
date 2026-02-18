from fastapi import FastAPI
import mysql.connector

app = FastAPI()

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mahitha!2002",  # change this
        database="school"
    )



# API to fetch students
@app.get("/students")
def get_students():
    connection = get_connection()
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ")
    data = cursor.fetchall()

    connection.close()

    return data
