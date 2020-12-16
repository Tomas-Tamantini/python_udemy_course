import os
import re

# Auxiliary variable/functions
io_folder_path = os.path.join('section13', 'io_files')


def get_file_path(file_name):
    file_path = os.path.join(io_folder_path, file_name)
    if not os.path.isfile(file_path):
        raise ValueError('Invalid file name')
    return file_path


# Exercise 7
def replace_vowels(file_name):
    """
    Saves new file with all vowels in input file text replaced by '*'
    :param file_name: Name of input file in folder io_files
    """

    try:
        file_path = get_file_path(file_name)
        with open(file_path, 'r') as file:
            original_text = file.read()
    except ValueError as err:
        print(str(err))
        return

    if len(original_text) == 0:
        return

    new_text = re.sub('[AEIOUaeiou]', '*', original_text)
    new_path = os.path.join(os.path.dirname(get_file_path(file_name)), 'ex_7_out.txt')

    with open(new_path, 'w') as file:
        file.write(new_text)


# Exercise 10
def biggest_city(file_name):
    """
    Saves new file with biggest city found in input text file
    :param file_name: Name of input file. Cities and populations should be listed one per line
    """
    try:
        file_path = get_file_path(file_name)
        with open(file_path, 'r') as file:
            cities_str = file.readlines()
    except ValueError as err:
        print(str(err))
        return

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

    new_path = os.path.join(os.path.dirname(get_file_path(file_name)), 'ex_10_out.txt')

    with open(new_path, 'w') as file:
        file.write(new_text)
