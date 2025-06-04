# parameters= ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "dew_point_2m", "precipitation_probability", "precipitation", "rain", "showers", "snowfall", "snow_depth", "weather_code", "pressure_msl", "surface_pressure", "cloud_cover", "cloud_cover_low", "cloud_cover_mid", "cloud_cover_high", "visibility", "et0_fao_evapotranspiration", "evapotranspiration", "vapour_pressure_deficit", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m", "wind_speed_180m", "wind_direction_10m", "wind_direction_80m", "wind_direction_120m", "wind_direction_180m", "wind_gusts_10m", "temperature_80m", "temperature_120m", "temperature_180m"]

class ParameterGen():
    def __init__(self,para):
        self.parameters=para
        # print(para)
        
        # print("parameters received")
        # print(self.paramaeter_hourly())

    def parameter_hourly(self):
    #    for i in self.parameters:
    #        print(i)
       return self.parameters
    
    def response(self):
        pass
        

    

