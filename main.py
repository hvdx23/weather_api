from openmateo import get_weather
from openmateoclass import WeatherAPI
from para_gen import ParameterGen

latitude= [-37.78,52.48]
longitude=[175.27,45.44]
parameters=[{}]
days=1
para=["temperature_2m", "relative_humidity_2m"]
# para=["temperature_2m"]

# data=get_weather(latitude,longitude,days)
weather_api = WeatherAPI(parameters)
parameters=ParameterGen(para)
main_parameters=parameters.parameter_hourly()
# print(main_parameters)


# print (main_parameters)

aus_data=weather_api.get_weather(56.23,45.21,main_parameters,1)
# other_data=weather_api.get_weather(12.32,54.43,para,1)
# print(data)