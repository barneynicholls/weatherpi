import http.client
import urllib.parse
from config import Config as cfg


class WeatherChannel(object):
    def log(self,logentry):
        # upload to thingspeak
        params = urllib.parse.urlencode({
            'field1': logentry.temperature,
            'field2': logentry.pressure,
            'field3': logentry.windspeed_avg,
            'field4': logentry.windspeed_max,
            'field5': logentry.wind_direction,
            'field6': logentry.rainfall,
            'field7': logentry.lux_ir,
            'field8': logentry.lux_visible,
            'key': cfg.ThingSpeak.WEATHER_CHANNEL_WRITE_KEY})
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        conn = http.client.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            data = response.read()
            conn.close()
        except:
            pass