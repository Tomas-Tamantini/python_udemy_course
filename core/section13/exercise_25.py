from datetime import datetime


# Models
class Contact:
    """
    Info about a person in your contact list
    """

    def __init__(self, name, phone_num='', birthday=None):
        self.name = name
        self.phone_num = phone_num
        self.birthday = birthday

    def __str__(self):
        b_day = self.birthday.strftime('%d/%m') if self.birthday is not None else ''
        return '; '.join([self.name, self.phone_num, b_day])


class ContactList:
    """
    A list of all contacts, each with their name, phone number and birthday
    """

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
