from datetime import datetime

from core.section13.exercise_25_s13 import Contact, ContactList
from core.utils.file_io_utils import file_exists, get_full_content, save_text
from core.utils.parser_utils import try_parse_int

db_file_name = 'ex_25'


def indexed_contact_to_str(indexed_contact):
    id, contact = indexed_contact
    return f'{id}. {str(contact).replace(";", " --- ")}'


def print_list_contacts(contacts):
    if len(contacts) == 0:
        print('No contacts...')
        return
    plural = 's' if len(contacts) != 1 else ''
    print(f'{len(contacts)} contact{plural}:\n\t' + '\n\t'.join(map(indexed_contact_to_str, contacts)))


def parse_contact(contact_str):
    fields = contact_str.split(';')
    if len(fields) != 3:
        print(f'Could not parse contact: "{contact_str}"')
        return None
    name = fields[0].strip()
    phone_num = fields[1].strip()
    try:
        birthday = datetime.strptime(fields[2].strip(), '%d/%m')
    except ValueError:
        print(f'Could not parse contact: "{contact_str}"')
        return None
    return Contact(name, phone_num, birthday)


def get_db_content():
    if not file_exists(db_file_name):
        return []
    contacts_str = get_full_content(db_file_name, split_by_lines=True)
    contacts = list(map(parse_contact, contacts_str))
    return list(filter(lambda x: x is not None, contacts))


def save_contact_list(contact_list):
    save_text(str(contact_list), db_file_name)


def main_loop():
    contacts = get_db_content()
    contact_list = ContactList(contacts)
    options = {'s': (show_all_contacts, 'Show all contacts'),
               'a': (add_new_contact, 'Add new contact'),
               'r': (remove_contact, 'Remove contact'),
               'n': (search_by_name, 'Search contacts by name'),
               'f': (search_by_first_letter, 'Search contacts by first letter'),
               'm': (search_by_birth_month, 'Search contacts by birth month')}
    help_str = 'Options:\n\t' + '\n\t'.join(map(lambda x: x[0] + ' - ' + x[1][1], options.items()))

    while True:
        cmd = input(f'Choose an option {tuple(options.keys())}, or press "q" to exit, or "h" for help: ')
        cmd = cmd.lower()
        if cmd == 'q':
            break
        if cmd == 'h':
            print(help_str)
            continue
        if cmd not in options.keys():
            print('Invalid option. Try again.')
            continue
        options[cmd][0](contact_list)

    save_contact_list(contact_list)


def show_all_contacts(contact_list):
    contacts = contact_list.all_contacts()
    print_list_contacts(contacts)


def add_new_contact(contact_list):
    name = input('Name: ')
    phone_num = input('Phone number: ')
    bday = input('Birthday (dd/mm): ')
    contact = parse_contact(';'.join((name, phone_num, bday)))
    if contact is None:
        print('Contact was NOT added. Try again')
        return
    contact_list.insert_contact(contact)
    print('Contact added successfully')


def remove_contact(contact_list):
    cmd = input('Contact index: ')
    could_parse, index = try_parse_int(cmd)
    if not could_parse:
        print('Invalid index')
        return
    contact_list.remove_contact(index)


def search_by_name(contact_list):
    name = input('Name: ').strip()
    contacts = contact_list.search_by_name(name)
    print_list_contacts(contacts)


def search_by_first_letter(contact_list):
    first_letter = input('First letter: ').strip()
    contacts = contact_list.search_by_first_letter(first_letter)
    print_list_contacts(contacts)


def search_by_birth_month(contact_list):
    current_month = datetime.now().month
    cmd = input(f'Type month as a number, or type "n" to use current month ({current_month}): ').strip()
    if cmd.lower() == 'n':
        month = current_month
    else:
        could_parse, month = try_parse_int(cmd)
        if not could_parse or month < 1 or month > 12:
            print('Invalid month')
            return
    contacts = contact_list.get_birthday_people(month)
    print_list_contacts(contacts)


if __name__ == '__main__':
    main_loop()
