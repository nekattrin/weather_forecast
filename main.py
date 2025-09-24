import streamlit as st
import plotly.express as px
from backend import get_data

sky_images = {'Clear': r'sky_images/clear.png',
              'Clouds': r'sky_images/cloud.png',
              'Rain': r'sky_images/rain.png',
              'Snow': r'sky_images/snow.png'}

st.title("Weather forecast for the next days")
place = st.text_input("City:")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days from 1 to 5")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))



if place:
    if days == 1:
        dayDays = "day"
    else:
        dayDays = "days"
    st.subheader(f"{option} for the next {days} {dayDays} in {place}")
    try:
        filtered_data = get_data(place, days)
        dates = [dict['dt_txt'] for dict in filtered_data]
        if option == "Temperature":
            temperatures = [(dict['main']['temp']-273.15) for dict in filtered_data]
            figure = px.line(x=dates, y=temperatures, labels={"x": "dates", "y": "temperatures(C)"},
                             markers=True)
            st.plotly_chart(figure)
        else:
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            images = [sky_images[condition] for condition in sky_conditions]
            st.image(images, width=115, caption=dates)
    except KeyError:
        st.text(f"There is no such city as {place}, try again.")





