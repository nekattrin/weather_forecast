import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather forecast for the next days")
place = st.text_input("City:")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days from 1 to 5")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if days == 1:
    dayDays = "day"
else:
    dayDays = "days"
st.subheader(f"{option} for the next {days} {dayDays} in {place}")


d, t = get_data(place, days, option)


figure = px.line(x=d, y=t, labels={"x": "dates", "y": "temperatures(C)"},
                 markers=True)
st.plotly_chart(figure)