class LogEntry:
    def __init__(self, temperature, pressure, windspeed_avg, windspeed_max, wind_direction, rainfall, lux_ir, lux_visible):
        self.temperature = temperature
        self.pressure = pressure
        self.windspeed_avg = windspeed_avg
        self.windspeed_max = windspeed_max
        self.wind_direction = wind_direction
        self.rainfall = rainfall
        self.lux_ir = lux_ir
        self.lux_visible = lux_visible