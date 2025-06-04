from openmateo import get_weather
from openmateoclass import WeatherAPI

latitude= [-37.78,52.48]
longitude=[175.27,45.44]
parameters=[{}]
days=1

# data=get_weather(latitude,longitude,days)
weather_api = WeatherAPI()

aus_data=weather_api.get_weather(56.23,45.21,10)

# print(data)