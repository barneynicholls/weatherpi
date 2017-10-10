import unittest


class RaspberryPiTest(unittest.TestCase):
    def testWindSpeedGpioPinSet(self):
        import config
        cfg = config.Config()
        self.assertGreater(cfg.RaspberryPi.WIND_SPEED_GPIO, 0, 'Wind Speed GPIO Pin Not Set')


if __name__ == '__main__':
    unittest.main()