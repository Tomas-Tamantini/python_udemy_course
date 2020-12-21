"""
The classes below are solutions to exercises 17 - 31 of section 17.
There is one super class (Appliance) from which Television and Microwave inherit
"""


class Appliance:
    def __init__(self, is_on=False):
        self._is_on = is_on

    def turn_on(self):
        self._is_on = True

    def turn_off(self):
        self._is_on = False

    def print_state(self):
        print(str(self))

    def __str__(self):
        return f'Appliance is {"on" if self._is_on else "off"}.'


class Television(Appliance):
    def __init__(self, channel=12, volume=5, is_on=False):
        super().__init__(is_on)
        self.__channel = channel
        self.__volume = volume
        self.__num_channels = 12
        self.__max_volume = 10

    def increment_channel(self):
        if not self._is_on:
            print("Can't change channels before turning on the TV.")
            return
        self.__channel = 1 if self.__channel >= 12 else self.__channel + 1

    def decrement_channel(self):
        if not self._is_on:
            print("Can't change channels before turning on the TV.")
            return
        self.__channel = 12 if self.__channel <= 1 else self.__channel - 1

    def increment_volume(self):
        if not self._is_on:
            print("Can't change volume before turning on the TV.")
            return
        if self.__volume < self.__max_volume:
            self.__volume += 1

    def decrement_volume(self):
        if not self._is_on:
            print("Can't change volume before turning on the TV.")
            return
        if self.__volume > 0:
            self.__volume -= 1

    def __str__(self):
        super_str = super().__str__().replace('Appliance', 'TV')
        if not self._is_on:
            return super_str
        return super_str + f'\n\tChannel: {self.__channel} (Available: 1 - {self.__num_channels})' + f'\n\tVolume: {self.__volume} (Range: 0 - {self.__max_volume})'


class Microwave(Appliance):
    def __init__(self, door_is_open=False, is_on=False):
        if door_is_open:
            if is_on:
                print("Microwave can't be on with the door open")
                is_on = False
        super().__init__(is_on)
        self.__door_is_open = door_is_open

    def open_door(self):
        self.__door_is_open = True
        self._is_on = False

    def close_door(self):
        self.__door_is_open = False

    def turn_on(self):
        if self.__door_is_open:
            print("Microwave can't be on with the door open")
            return
        super().turn_on()

    def __str__(self):
        super_str = super().__str__()
        return super_str.replace('Appliance',
                                 'Microwave') + f'\n\tThe door is {"open" if self.__door_is_open else "closed"}'
