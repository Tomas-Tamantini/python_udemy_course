from section13 import solution_section_13


def main():
    funcs = {13: solution_section_13.main}
    accepted_inputs = tuple(funcs.keys())
    while True:
        inp = input(f'Enter a section {accepted_inputs} or "q" to return: ')
        if inp == 'q' or inp == 'Q':
            return

        try:
            section = int(inp)
        except ValueError:
            print('Invalid section.')
            continue

        if section not in accepted_inputs:
            print('Invalid section.')
            continue

        funcs[section]()


if __name__ == '__main__':
    main()
