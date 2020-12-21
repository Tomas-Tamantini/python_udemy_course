from core.section16.exercise_04_s16 import Remote, Television
from core.utils.parser_utils import try_parse_int


def main_loop():
    tv = Television()
    print(tv)
    remote = Remote(tv)
    while True:
        cmd = input('Choose option ("i", "d", "u", "w", "s"), or press "q" to return, or "h" for help: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 'h':
            print('Options:\n\t'
                  'i - Increase volume\n\t'
                  'd - Decrease volume\n\t'
                  'u - Go up by one channel\n\t'
                  'w - Go down by one channel\n\t'
                  's - Set channel')
        elif cmd == 'i':
            remote.increment_volume()
            print(f'Volume is now {tv.volume}')
        elif cmd == 'd':
            remote.decrement_volume()
            print(f'Volume is now {tv.volume}')
        elif cmd == 'u':
            remote.increment_channel()
            print(f'Now at channel {tv.channel}')
        elif cmd == 'w':
            remote.decrement_channel()
            print(f'Now at channel {tv.channel}')
        elif cmd == 's':
            new_channel_str = input('Enter channel: ')
            could_parse, new_channel = try_parse_int(new_channel_str)
            if not could_parse:
                print('Invalid channel')
                continue
            remote.set_channel(new_channel)
            print(f'Now at channel {tv.channel}')
        else:
            print('Invalid option. Try again.')


if __name__ == '__main__':
    main_loop()
