import streamlit as st
import requests
import geocoder

API_KEY = "9f94ebfd84c23750c837ae2f672bda82"

st.set_page_config(page_title="Weather Dashboard", layout="centered")

st.title("🌦 Weather Dashboard")
st.write("Get real-time weather information for any city")

def detect_location():
    try:
        g = geocoder.ip('me')
        return g.city
    except:
        return None

city = st.text_input("Enter City Name")

col1, col2 = st.columns(2)

with col1:
    if st.button("📍 Use My Location"):
        city = detect_location()
        if city:
            st.success(f"Detected Location: {city}")
        else:
            st.error("Could not detect location")

with col2:
    unit = st.selectbox("Temperature Unit", ["Celsius", "Fahrenheit"])

if unit == "Celsius":
    units = "metric"
    symbol = "°C"
else:
    units = "imperial"
    symbol = "°F"

def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": units
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code != 200:
            st.error(data.get("message", "City not found"))
            return

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        description = data["weather"][0]["description"]
        icon = data["weather"][0]["icon"]

        icon_url = f"http://openweathermap.org/img/wn/{icon}@2x.png"

        st.image(icon_url, width=120)

        st.subheader(f"Weather in {city.title()}")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown(
                f"<div style='background:white;padding:15px;border-radius:10px;text-align:center;color:black;'>"
                f" Temperature<br><b>{temp} {symbol}</b></div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div style='background:white;padding:15px;border-radius:10px;text-align:center;color:black;margin-top:10px;'>"
                f" Humidity<br><b>{humidity}%</b></div>",
                unsafe_allow_html=True
            )

        with col2:
            st.markdown(
                f"<div style='background:white;padding:15px;border-radius:10px;text-align:center;color:black;'>"
                f" Wind Speed<br><b>{wind} m/s</b></div>",
                unsafe_allow_html=True
            )

            st.markdown(
                f"<div style='background:white;padding:15px;border-radius:10px;text-align:center;color:black;margin-top:10px;'>"
                f" Condition<br><b>{description.title()}</b></div>",
                unsafe_allow_html=True
            )

    except:
        st.error("Unable to fetch weather data. Check internet connection or API key.")

if st.button(" Get Weather"):

    if city.strip() == "":
        st.warning("Please enter a city name")
    else:
        get_weather(city)

st.markdown("---")
st.write("Stay informed with real-time weather updates.")
