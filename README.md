# Weather App

## Overview
This Weather App is a simple web application built with Flask that fetches real-time weather data using the OpenWeatherMap API. Users can enter a city name, and the app will display the current temperature, humidity, and wind speed in a visually appealing interface.

## Features
- Fetches real-time weather data based on user input.
- Displays temperature (in Fahrenheit), humidity, and wind speed.
- User-friendly UI with a modern, responsive design.
- Error handling for invalid city names.

## Technologies Used
- **Backend:** Flask (Python)
- **Frontend:** HTML, CSS
- **API:** OpenWeatherMap
- **Styling:** DM Sans font, CSS animations, and Glassmorphism effect

## Installation & Setup
### Prerequisites
- Python 3.x installed
- Flask installed (`pip install flask`)
- Requests library installed (`pip install requests`)
- OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/) and get your API key)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/weather-app.git
   cd weather-app
   ```
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate  # On Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env.local` file and add your OpenWeatherMap API key:
   ```
   api_key=YOUR_API_KEY_HERE
   ```
5. Run the Flask app:
   ```bash
   python app.py
   ```
6. Open your browser and visit `http://127.0.0.1:5000/`.

## Usage
1. Enter a city name in the search box.
2. Click "Get Weather".
3. View the temperature, humidity, and wind speed.

## Future Improvements
- Add weather icons and descriptions.
- Display a 5-day weather forecast.
- Implement geolocation to get weather based on the user's location.
- Improve UI with additional styling and animations.

## License
This project is open-source and available under the [MIT License](LICENSE).

