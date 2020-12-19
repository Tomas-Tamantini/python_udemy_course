class Television:
    def __init__(self, volume=5, channel=12):
        self.__volume = volume
        self.__channel = channel

    @property
    def channel(self):
        return self.__channel

    @property
    def volume(self):
        return self.__volume

    def increment_volume(self):
        if self.volume < 10:
            self.__volume += 1

    def decrement_volume(self):
        if self.volume > 1:
            self.__volume -= 1

    def increment_channel(self):
        self.__channel += 1
        if self.channel > 12:
            self.__channel = 3

    def decrement_channel(self):
        self.__channel -= 1
        if self.channel < 3:
            self.__channel = 12

    def set_channel(self, channel_num):
        if 3 <= channel_num <= 12:
            self.__channel = channel_num

    def __str__(self):
        return f'Currently at channel {self.__channel}. The volume is {self.__volume}'


class Remote:
    def __init__(self, tv):
        self.__tv = tv

    def increment_volume(self):
        self.__tv.increment_volume()

    def decrement_volume(self):
        self.__tv.decrement_volume()

    def increment_channel(self):
        self.__tv.increment_channel()

    def decrement_channel(self):
        self.__tv.decrement_channel()

    def set_channel(self, channel_num):
        self.__tv.set_channel(channel_num)

    def __str__(self):
        return f'Remote control associated to TV: {str(self.__tv)}'
