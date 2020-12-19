import unittest

from core.section16.exercise_04_s16 import Television, Remote


class TestRemote(unittest.TestCase):
    def setUp(self):
        self.tv = Television(volume=5, channel=12)
        self.remote = Remote(self.tv)

    def test_volume(self):
        for i in range(6):
            self.remote.increment_volume()
            expected_volume = min(6 + i, 10)
            actual_volume = self.tv.volume
            self.assertEqual(expected_volume, actual_volume)

    def test_channel(self):
        for i in range(6):
            self.remote.increment_channel()
            expected_channel = 3 + i
            actual_channel = self.tv.channel
            self.assertEqual(expected_channel, actual_channel)

        self.remote.set_channel(4)
        expected_channel = 4
        actual_channel = self.tv.channel
        self.assertEqual(expected_channel, actual_channel)

        self.remote.set_channel(1234)
        expected_channel = 4
        actual_channel = self.tv.channel
        self.assertEqual(expected_channel, actual_channel)


if __name__ == '__main__':
    unittest.main()
