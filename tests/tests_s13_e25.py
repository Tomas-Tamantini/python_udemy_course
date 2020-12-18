import unittest
from datetime import date

from core.section13.exercise_25 import ContactList, Contact


class TestContacts(unittest.TestCase):
    def setUp(self):
        contacts = [
            Contact('Ataw Wallpa', '801-993-9313', date(1502, 3, 30)),
        ]
        self.contact_list = ContactList(contacts)

    def test_get_all_contacts(self):
        contacts = self.contact_list.all_contacts()
        expected_num_contacts = 1
        actual_num_contacts = len(contacts)
        self.assertEqual(expected_num_contacts, actual_num_contacts)

        expected_name = 'Ataw Wallpa'
        actual_name = contacts[0][1].name
        self.assertEqual(expected_name, actual_name)

    def test_insert(self):
        new_contact = Contact('Tupac Cusi', '(29) 45873-1571', date(1491, 4, 1))
        self.contact_list.insert_contact(new_contact)
        contacts = self.contact_list.contacts
        expected_num_contacts = 2
        self.assertEqual(expected_num_contacts, len(contacts))

        expected_name = 'Tupac Cusi'
        actual_name = contacts[1].name
        self.assertEqual(expected_name, actual_name)


if __name__ == '__main__':
    unittest.main()
