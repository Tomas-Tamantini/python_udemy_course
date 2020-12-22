from core.section17.exercise_17_s17 import Television, Microwave


def main_loop():
    while True:
        cmd = input('Choose an appliance to work with - "t" (TV) or "m" (Microwave), or press "q" to return: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 't':
            loop_tv()
        elif cmd == 'm':
            loop_microwave()
        else:
            print('Invalid option. Try again.')


def loop_tv():
    tv = Television()
    print(tv)
    while True:
        cmd = input('Choose option ("t", "f", "i", "d", "u", "w"), or press "q" to return, or "h" for help: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 'h':
            print('Options:\n\t'
                  't - Turn on TV\n\t'
                  'f - Turn off TV\n\t'
                  'i - Increase volume\n\t'
                  'd - Decrease volume\n\t'
                  'u - Go up by one channel\n\t'
                  'w - Go down by one channel')
            continue
        if cmd not in ('t', 'f', 'i', 'd', 'u', 'w'):
            print('Invalid command. Try again')
            continue
        if cmd == 't':
            tv.turn_on()
        elif cmd == 'f':
            tv.turn_off()
        elif cmd == 'i':
            tv.increment_volume()
        elif cmd == 'd':
            tv.decrement_volume()
        elif cmd == 'u':
            tv.increment_channel()
        elif cmd == 'w':
            tv.decrement_channel()
        print(tv)


def loop_microwave():
    mw = Microwave()
    print(mw)
    while True:
        cmd = input('Choose option ("t", "f", "d", "c"), or press "q" to return, or "h" for help: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 'h':
            print('Options:\n\t'
                  't - Turn on microwave\n\t'
                  'f - Turn off microwave\n\t'
                  'd - Open microwave door\n\t'
                  'c - Close microwave door')
            continue
        if cmd not in ('t', 'f', 'd', 'c'):
            print('Invalid command. Try again')
            continue
        if cmd == 't':
            mw.turn_on()
        elif cmd == 'f':
            mw.turn_off()
        elif cmd == 'd':
            mw.open_door()
        elif cmd == 'c':
            mw.close_door()
        print(mw)


if __name__ == '__main__':
    main_loop()
