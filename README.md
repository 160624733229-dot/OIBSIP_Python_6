# OIBSIP_Python_6
# 🌦 Weather Dashboard

A simple and interactive Weather Dashboard built using Python and Streamlit.

This application allows users to:
- Search weather by city
- Detect their current location automatically
- View temperature, humidity, wind speed, and weather condition
- Switch between Celsius and Fahrenheit units
- See weather icons for visual understanding

## Features

- Real-time weather data
- Location detection
- Clean UI layout
- Weather icons
- Error handling

## Technologies Used

- Python
- Streamlit
- OpenWeather API
- Requests
- Geocoder

## Installation

1. Clone the repository

git clone https://github.com/yourusername/weather-dashboard-streamlit.git

2. Navigate into the project folder

cd weather-dashboard-streamlit

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run weather_adv.py

## API Key Setup

Create a free API key from OpenWeather:

https://openweathermap.org/api

Then replace:

API_KEY = "YOUR_API_KEY_HERE"

with your API key.

## Example Output

Displays:
- Temperature
- Humidity
- Wind Speed
- Weather Condition
- Weather Icon

## Future Improvements

- 5-day forecast
- Weather charts
- Dark mode
- Hourly weather data