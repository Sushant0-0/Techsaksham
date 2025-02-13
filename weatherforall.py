import streamlit as st
import requests
import datetime


# Function to fetch weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']
        icon = weather['icon']

        return {
            "temperature": temperature,
            "pressure": pressure,
            "humidity": humidity,
            "description": description,
            "icon": icon
        }
    else:
        return None


# Streamlit UI setup
st.title("Weather App")
st.write("Enter a city name to get the current weather information:")

# User input for city
city = st.text_input("City Name", "London")

# Replace with your OpenWeatherMap API key
API_KEY = "2412aa7c770c725bbde968b8280b3dc3"

if city:
    weather_data = get_weather(city, API_KEY)

    if weather_data:
        # Display the weather data
        st.subheader(f"Weather in {city.title()}")
        st.write(f"Temperature: {weather_data['temperature']} °C")
        st.write(f"Pressure: {weather_data['pressure']} hPa")
        st.write(f"Humidity: {weather_data['humidity']} %")
        st.write(f"Description: {weather_data['description'].capitalize()}")

        # Show weather icon
        icon_url = f"http://openweathermap.org/img/wn/{weather_data['icon']}@2x.png"
        st.image(icon_url, width=100)
    else:
        st.error(f"Could not fetch weather data for {city}. Please try again.")
