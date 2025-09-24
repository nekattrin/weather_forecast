import requests
import streamlit as st
import os

api_key = st.secrets["WEATHER_API_KEY"]

def get_data(place, forecast_days=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data


#this part is triggered only ef we execute this file
if __name__ == "__main__":
    print(get_data("Tokyo", 3))

