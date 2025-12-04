import streamlit as st
import requests
from dotenv import load_dotenv
import os

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

st.set_page_config(page_title="Weather App", page_icon="🌤️", layout="centered")

st.title("Real-Time Weather App 🌍")
st.markdown("Enter a city name to get current weather")

city = st.text_input("City Name", placeholder="e.g., Punjab, Mumbai, country Name")

if st.button("Get Weather"):
    if city:
        with st.spinner("Fetching weather data..."):
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                temp = data['main']['temp']
                feels_like = data['main']['feels_like']
                humidity = data['main']['humidity']
                description = data['weather'][0]['description'].capitalize()
                icon = data['weather'][0]['icon']

                col1, col2 = st.columns([1, 2])
                with col1:
                    st.image(f"http://openweathermap.org/img/wn/{icon}@4x.png")
                with col2:
                    st.metric("Temperature", f"{temp}°C", f"Feels like {feels_like}°C")
                    st.write(f"**Condition:** {description}")
                    st.write(f"**Humidity:** {humidity}%")

                st.success(f"Weather in {city.title()} updated!")
            else:
                st.error(f"City '{city}' not found! Please try again.")
    else:
        st.warning("Please enter a city name.")

st.markdown("---")
st.caption("Powered by OpenWeatherMap | Made with Streamlit")