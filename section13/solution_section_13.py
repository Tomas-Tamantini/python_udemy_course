import re

# Exercise 7
from io_helper import file_exists, file_path, save_text


def replace_vowels(file_name):
    """
    Saves new file with all vowels in input file text replaced by '*'
    :param file_name: Name of input file in folder io_files
    """

    if not file_exists(file_name, section=13):
        print(f'Input file {file_name} was not found')
        return

    input_path = file_path(file_name, section=13)

    with open(input_path, 'r') as file:
        original_text = file.read()

    if len(original_text) == 0:
        return

    new_text = re.sub('[AEIOUaeiou]', '*', original_text)
    save_text(new_text, 'ex_7_out.txt', section=13)


# Exercise 10
def biggest_city(file_name):
    """
    Saves new file with biggest city found in input text file
    :param file_name: Name of input file. Cities and populations should be listed one per line
    """

    if not file_exists(file_name, section=13):
        print(f'Input file {file_name} was not found')
        return

    input_path = file_path(file_name, section=13)

    with open(input_path, 'r') as file:
        cities_str = file.readlines()

    def parse_city(city_str):
        clean_str = city_str.strip()
        split_pos = clean_str.rfind(' ')
        city_name, city_pop_str = clean_str[:split_pos], clean_str[split_pos:]
        population = 0
        try:
            population = int(city_pop_str)
        except ValueError:
            print(f'Could not parse city population: {city_str}')
        return city_name.strip(), population

    cities = list(map(parse_city, cities_str))
    biggest = sorted(cities, key=lambda city: city[1], reverse=True)[0]
    new_text = f'City with the largest population:\n\t- {biggest[0]} - {biggest[1]}'
    save_text(new_text, 'ex_10_out.txt', section=13)


def main():
    funcs = {7: replace_vowels, 10: biggest_city}
    accepted_inputs = tuple(funcs.keys())
    while True:
        inp = input(f'Enter an exercise {accepted_inputs} or "q" to return: ')
        if inp == 'q' or inp == 'Q':
            return

        try:
            num = int(inp)
        except ValueError:
            print('Invalid exercise.')
            continue

        if num not in accepted_inputs:
            print('Invalid exercise.')
            continue

        file_name = input('Enter file name: ')
        funcs[num](file_name.strip())


if __name__ == '__main__':
    main()
