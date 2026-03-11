import requests

API_KEY = "5431c9f5d3f49ba3c851523632a6d9d5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

response = requests.get(BASE_URL, params=params)

if response.status_code == 200:
    data = response.json()
    print("data received successfully", data)

    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    country = data["sys"]["country"]
    description = data["weather"][0]["description"]

    print("\nWeather Report 🌦️")
    print("Country:", country)  
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", description)

else:
    print("City not found ❌")
