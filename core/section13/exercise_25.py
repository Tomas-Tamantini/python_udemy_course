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

    def all_contacts(self):
        return list(enumerate(self.contacts))

    def insert_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact_idx):
        if contact_idx < 0 or contact_idx >= len(self.contacts):
            print('Invalid index')
        else:
            del self.contacts[contact_idx]
            print('Contact deleted successfully')

    def search_by_name(self, name):
        return self._search_contact(match_function=lambda contact: contact.name.lower() == name.lower().strip())

    def search_by_first_letter(self, first_letter):
        return self._search_contact(
            match_function=lambda contact: contact.name[0].lower() == first_letter.lower().strip())

    def get_birthday_people(self, month=None):
        if month is None:
            month = datetime.now().month

        def match_function(contact):
            return month == contact.birthday.month

        return self._search_contact(match_function)

    def _search_contact(self, match_function):
        return list(filter(lambda indexed_contact: match_function(indexed_contact[1]), enumerate(self.contacts)))
