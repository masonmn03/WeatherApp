import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('api_key')

url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={api_key}"
response = requests.get(url)

if response.status_code == 200:
    print("API key works:", response.json())
else:
    print("Error:", response.status_code, response.json())
