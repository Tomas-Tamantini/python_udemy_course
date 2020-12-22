from core.section17.exercise_3_s17 import Circle, Rectangle, Square
from core.utils.parser_utils import try_parse_float


def main_loop():
    while True:
        cmd = input('Choose a planar shape to work with - '
                    '"c" (Circle), "s" (Square) or "r" (Rectangle), or press "q" to return: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 'c':
            loop_circle()
        elif cmd == 's':
            loop_square()
        elif cmd == 'r':
            loop_rectangle()
        else:
            print('Invalid option. Try again.')


def loop_rectangle():
    while True:
        rectangle_dims = {'width': 0, 'height': 0}
        for dim in ('width', 'height'):
            cmd = input(f'Enter rectangle {dim}, or press "q" to return: ')
            cmd = cmd.lower()
            if cmd == 'q':
                break
            could_parse, length = try_parse_float(cmd)
            if not could_parse or length < 0:
                print(f'Invalid {dim}. Try again')
                continue
            rectangle_dims[dim] = length
        r = Rectangle(*rectangle_dims.values())
        print(r)
        break


def loop_square():
    while True:
        cmd = input('Enter square side length, or press "q" to return: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        could_parse, side_length = try_parse_float(cmd)
        if not could_parse or side_length < 0:
            print('Invalid side length. Try again')
            continue
        s = Square(side_length)
        print(s)
        break


def loop_circle():
    while True:
        cmd = input('Enter circle radius, or press "q" to return: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        could_parse, radius = try_parse_float(cmd)
        if not could_parse or radius < 0:
            print('Invalid radius. Try again')
            continue
        c = Circle(radius)
        print(c)
        break


if __name__ == '__main__':
    main_loop()
