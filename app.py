from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv('.env.local')
api_key = os.getenv('api_key')

def fetch_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature_kelvin = data['main']['temp']
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
        description = data['weather'][0]['description']
        return {
            'city': data['name'],
            'temperature': f"{temperature_fahrenheit:.2f}°F",
            'description': description
        }
    else:
        return None

def main():
    while True:
        city = input("Enter the city name or type 'exit' to quit: ")
        if city.lower() == 'exit':
            print("Exiting the program...")
            break
        temperature = get_temperature(city)
        if temperature is None:
            print("Error getting weather data. Please try again.")
            continue

        print(f"The temperature in {city} is {temperature:.2f}°F")

@app.route('/')
def home():
    return "<p>Weather API is running!</p>"

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')  # Get city from query parameters
    if not city:
        return jsonify({'error': 'City parameter is required'}), 400

    weather_data = fetch_weather(city)
    if weather_data is None:
        return jsonify({'error': 'City not found or error fetching data'}), 404

    return jsonify(weather_data)


if __name__ == "__main__":
    app.run(debug=True)
    main()
