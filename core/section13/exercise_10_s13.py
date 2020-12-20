# Exercise 10 - Read file of cities w/ population, find largest city and save it to new file
from core.utils.file_io_utils import save_text, get_full_content


def parse_city(city_str):
    """
    Returns tuple with city name and population from string separated by space
    """
    clean_str = city_str.strip()
    split_pos = clean_str.rfind(' ')
    city_name, city_pop_str = clean_str[:split_pos], clean_str[split_pos:]
    population = 0
    try:
        population = int(city_pop_str)
    except ValueError:
        print(f'Could not parse city population: {city_str}')
    return city_name.strip(), population


def biggest_city(file_name):
    """
    Saves new file with biggest city found in input text file
    :param file_name: Name of input file. Cities and populations should be listed one per line
    """
    cities_str = get_full_content(file_name, split_by_lines=True)

    if cities_str is None:
        return

    cities = list(map(parse_city, cities_str))
    biggest = sorted(cities, key=lambda city: city[1], reverse=True)[0]
    new_text = f'City with the largest population:\n\t- {biggest[0]} - {biggest[1]}'
    save_text(new_text, 'ex_10_out', overwrite=True)
