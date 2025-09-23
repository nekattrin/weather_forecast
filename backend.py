import requests
import os

api_key = os.getenv('WEATHER_API_KEY')

def get_data(place, forecast_days=None, data_kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    if data_kind == "Temperature":
        filtered_data = [dict['main']['temp'] for dict in filtered_data]
    else:
        filtered_data = [dict['weather'][0]['main'] for dict in filtered_data]

    return filtered_data


#this part is triggered only ef we execute this file
if __name__ == "__main__":
    print(get_data("Tokyo", 3, "Temperature"))

