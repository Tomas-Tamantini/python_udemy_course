# Exercise 25
# Models
from datetime import datetime

from common_parsers import int_parser
from io_helper import file_exists, file_path, get_full_content


class Contact:
    def __init__(self, name, phone_num='', birthday=None):
        self.name = name
        self.phone_num = phone_num
        self.birthday = birthday

    def __str__(self):
        b_day = self.birthday.strftime('%d/%m') if self.birthday is not None else ''
        return '; '.join([self.name, self.phone_num, b_day])


class ContactList:
    def __init__(self, contacts):
        self.contacts = contacts

    def show_all_contacts(self):
        if len(self.contacts) == 0:
            print('No contacts have been saved yet.')
        else:
            print('\n'.join(map(lambda c: f'{c[0]}. {str(c[1])}', enumerate(self.contacts))))

    def insert_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact_idx):
        if contact_idx < 0 or contact_idx >= len(self.contacts):
            print('Invalid index')
        else:
            del self.contacts[contact_idx]

    def search_by_name(self, name):
        self._search_contact(match_function=lambda contact: contact.name.lower() == name.lower().strip())

    def search_by_first_letter(self, first_letter):
        self._search_contact(match_function=lambda contact: contact.name[0].lower() == first_letter.lower().strip())

    def get_birthday_people(self, month=None):
        if month is None:
            month = datetime.now().month

        def match_function(contact):
            return month == contact.birthday.month

        self._search_contact(match_function)

    def _search_contact(self, match_function):
        def filter_lambda(indexed_contact):
            _, contact = indexed_contact
            return match_function(contact)

        found_contacts = list(filter(filter_lambda, enumerate(self.contacts)))
        if len(found_contacts) == 0:
            print('No contacts found')
            return
        print('Contacts found: ')
        print(
            '\n'.join(map(lambda indexed_contact: f'{indexed_contact[0]}. {str(indexed_contact[1])}', found_contacts)))


def get_contact_list(file_name):
    contacts_str = get_full_content(file_name, section=13, split_by_lines=True)
    if contacts_str is None:
        return
    contacts = []
    for line in contacts_str:
        contact = get_contact_from_str(line)
        if contact is not None:
            contacts.append(contact)
    return ContactList(contacts)


# I/O functions
def get_contact_from_str(contact_str):
    str_fields = contact_str.split(';')
    if len(str_fields) < 3:
        print('Missing field, contact ignored in line: ' + contact_str)
        return None
    name = str_fields[0].strip()
    phone_num = str_fields[1].strip()
    try:
        birthday = datetime.strptime(str_fields[2].strip(), '%d/%m')
    except ValueError:
        print('Invalid birthday, contact ignored in line: ' + contact_str)
        return None
    return Contact(name, phone_num, birthday)


def manage_contacts(file_name='ex_25'):
    contacts = get_contact_list(file_name)
    action_dict = {'i': contacts.insert_contact, 's': contacts.show_all_contacts}
    possible_actions = tuple(action_dict.keys())
    while True:
        inp = input(f'Choose an action {possible_actions}, or press "h" for help, or "q" to return: ')
        if inp == 'q' or inp == 'Q':
            return
        if inp == 'h' or inp == 'H':
            print('s - Show all contacts\n')
            continue
        if inp not in possible_actions:
            print('Invalid action.')
            continue
        if inp == 'i':
            pass
        else:
            action_dict[inp]()
