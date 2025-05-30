from openmateo import get_weather

latitude= -37.78
longitude=175.27
parameters=[{}]
days=1

data=get_weather(latitude,longitude,days)
print(data)