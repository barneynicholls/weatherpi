import unittest


class ConfigurationTests(unittest.TestCase):
    def testThingSpeakSettings(self):
        import config
        cfg = config.Config()
        self.assertNotEqual(cfg.ThingSpeak.KEY, 'your_thingspeak_key_for_the_channel_you_upload_to',
                            'thingspeak channel key not set')

    def testRaspberryPiSettings(self):
        import config
        cfg = config.Config()
        self.assertGreater(cfg.RaspberryPi.WIND_SPEED_GPIO, -1,
                           'wind speed gpio pin not set')
        self.assertGreater(cfg.RaspberryPi.I2C_INTERFACE_BUS, -1,
                           'i2c interface bus not set')

    def testTwitterSettings(self):
        import config
        cfg = config.Config()
        self.assertNotEqual(cfg.Twitter.ACCESS_TOKEN, 'your_twitter_access_token',
                            'twitter access token not set')
        self.assertNotEqual(cfg.Twitter.ACCESS_TOKEN_SECRET, 'your_twitter_access_token_secret',
                            'twitter access token secret not set')
        self.assertNotEqual(cfg.Twitter.CONSUMER_KEY, 'your_twitter_consumer_key',
                            'twitter consumer key not set')
        self.assertNotEqual(cfg.Twitter.CONSUMER_SECRET, 'your_twitter_consumer_secret',
                            'twitter consumer secret not set')


if __name__ == '__main__':
    unittest.main()