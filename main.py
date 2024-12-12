import requests
from dotenv import load_dotenv
import os

load_dotenv('.env.local')
api_key = os.getenv('api_key')

city = input("Enter the city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature_kelvin = data['main']['temp']
    temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32

    print(f"The temperature in {city} is {temperature_fahrenheit:.2f}°F")
else:
    print("Error getting weather data")

#Testing changes
