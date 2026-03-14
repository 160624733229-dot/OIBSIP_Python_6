import requests

# ---------------- API KEY ----------------
API_KEY = "9f94ebfd84c23750c837ae2f672bda82"

# ---------------- FUNCTION ----------------
def get_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if data["cod"] != 200:
            print("\n❌ City not found. Please enter a valid city name.")
            return

        # Extract weather details
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        condition = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        # Display result
        print("\n🌍 Weather Information")
        print("----------------------------")
        print("City:", city.title())
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Condition:", condition.title())
        print("Wind Speed:", wind_speed, "m/s")
        print("----------------------------")

    except requests.exceptions.RequestException:
        print("⚠ Network error. Please check your internet connection.")


# ---------------- MAIN PROGRAM ----------------
def main():

    print("=================================")
    print("        BASIC WEATHER APP        ")
    print("=================================")

    city = input("Enter city name: ")

    if city.strip() == "":
        print("⚠ City name cannot be empty.")
        return

    get_weather(city)


# ---------------- RUN PROGRAM ----------------
if __name__ == "__main__":
    main()
