import requests
import pandas as pd
from datetime import datetime

# Define API endpoint and parameters
api_key = 'f1d7b7e9ce2bc4c7d82f2e73b500a8ba'  # Replace with your OpenWeatherMap API key
city_name = 'Dortmund'   # Replace with the name of the city you want to get weather data for
start_date = datetime(2022, 1, 1)  # Start date for weather data
end_date = datetime.now()         # End date for weather data (current date and time)
num_hours = int((end_date - start_date).total_seconds() / 3600)  # Calculate the number of hours between start and end date
num_6_hours = num_hours // 3  # Calculate the number of 6-hour intervals in the time period
base_url = 'https://api.openweathermap.org/data/2.5/forecast'
params = {
    'q': city_name,
    'cnt': num_6_hours,  # Set cnt parameter to number of 6-hour intervals
    'start_date': int(start_date.timestamp()),
    'appid': api_key
}

# Make API request
response = requests.get(base_url, params=params)
data = response.json()

# Extract relevant data from API response
weather_data = data['list']
weather_df = pd.DataFrame(weather_data)

# Clean up the dataframe
weather_df = weather_df[['dt', 'main', 'weather']]
weather_df['date'] = pd.to_datetime(weather_df['dt'], unit='s')
weather_df['temperature'] = weather_df['main'].apply(lambda x: x['temp'] - 273.15)
weather_df['weather_description'] = weather_df['weather'].apply(lambda x: x[0]['description'])

# Drop unnecessary columns
weather_df = weather_df.drop(columns=['dt', 'main', 'weather'])

# Print the resulting dataframe
print(weather_df)
