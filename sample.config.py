class TwitterConfig:
    API_KEY = 'twitter api key'
    SECRET = 'twitter secret'


class RaspberryPiConfig:
    WIND_SPEED_GPIO = 0


class Config:
    Twitter = TwitterConfig()
    RaspberryPi = RaspberryPiConfig()