from flask import Flask, request, jsonify, render_template
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__, static_folder='static')

load_dotenv('.env.local')
api_key = os.getenv('api_key')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city = request.form['city']
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        data = response.json()

        temperature_kelvin = data['main']['temp']
        temperature_fahrenheit = (temperature_kelvin - 273.15) * 9/5 + 32
        temperature = f"{temperature_fahrenheit:.2f}"
        
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        wind_mph = f"{wind * 2.23694:.2f}"

        return render_template('index.html', temperature=temperature, humidity=humidity, wind=wind_mph)
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)

