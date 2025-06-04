import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from para_gen import ParameterGen

cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

class WeatherAPI:
    
    def __init__(self,parameters):
        # Initialize the Open-Meteo API client with cache and retry settings
        cache_session = requests_cache.CachedSession('.cache', expire_after=3600)
        retry_session = retry(cache_session, retries=5, backoff_factor=0.2)
        self.client = openmeteo_requests.Client(session=retry_session)
        print("ClientAPI done")


    def get_weather(self, latitude, longitude,para, days):
        url = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "hourly": para,
            "timezone": "Australia/Sydney",
            "forecast_days": days
        }
        print(f'Lat={latitude}, Long={longitude}')
        responses = self.client.weather_api(url, params=params)

        
        
        response = responses[0]
        hourly = response.Hourly()
        # Hourly response to be generated


        hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
        hourly_relative_humidity_2m = hourly.Variables(1).ValuesAsNumpy()


# Hourly data to be generated and put here dynamically

        hourly_data = {
            "date": pd.date_range(
                start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                freq=pd.Timedelta(seconds=hourly.Interval()),
                inclusive="left"
            ),
            "temperature_2m": hourly_temperature_2m,
            "relative_humidity_2m": hourly_relative_humidity_2m
        }

        hourly_dataframe = pd.DataFrame(data=hourly_data)
        print(hourly_dataframe)
        return hourly_dataframe