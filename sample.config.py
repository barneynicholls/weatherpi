class TwitterConfig:
    CONSUMER_KEY = 'your_twitter_consumer_key'
    CONSUMER_SECRET = 'your_twitter_consumer_secret'
    ACCESS_TOKEN = 'your_twitter_access_token'
    ACCESS_TOKEN_SECRET = 'your_twitter_access_token_secret'


class RaspberryPiConfig:
    # I2C Interface bus. Rev 1 Pi uses 0, Rev 2 Pi uses 1
    I2C_INTERFACE_BUS = -1
    # gpio pin wind speed anemometer is connected to
    WIND_SPEED_GPIO = -1

class ThingSpeakConfig:
    WEATHER_CHANNEL_WRITE_KEY = 'your_thingspeak_key_for_the_channel_you_upload_to'

class Config:
    Twitter = TwitterConfig()
    RaspberryPi = RaspberryPiConfig()
    ThingSpeak = ThingSpeakConfig()