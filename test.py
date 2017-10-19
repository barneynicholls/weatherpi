import Loggers.Shared
import Loggers.ThingSpeak

print('calling weather channel')

wc = Loggers.ThingSpeak.WeatherChannel()

le = Loggers.Shared.LogEntry(
    lux_ir=1,
    lux_visible=2,
    temperature=23.7,
    pressure=1016,
    wind_direction='E',
    windspeed_max=47.2,
    windspeed_avg=23.5,
    rainfall=0)

wc.log(le)

print('done')

