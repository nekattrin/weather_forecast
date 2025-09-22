import streamlit as st
import plotly.express as px

st.title("Weather forecast for the next days")
place = st.text_input("Place:")
days = st.slider("Forecast days", min_value=1, max_value=5,
                 help="Select the number of forecasted days from 1 to 5")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))

if days == 1:
    dayDays = "day"
else:
    dayDays = "days"
st.subheader(f"{option} for the next {days} {dayDays} in {place}")


def get_data(days):
    dates =["2025-09-23", "2025-09-24", "2025-09-25", "2025-09-26", "2025-09-27"]
    dates = dates[:days]
    temperatures = [14, 15, 10, 11, 13]
    temperatures = temperatures[:days]
    return dates, temperatures

d, t = get_data(days)

figure = px.line(x=d, y=t, labels={"x": "dates", "y": "temperatures(C)"},
                 markers=True)
st.plotly_chart(figure)