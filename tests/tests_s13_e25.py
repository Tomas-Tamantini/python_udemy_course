import unittest
from datetime import date

from core.section13.exercise_25_s13 import ContactList, Contact


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

    def test_search_contacts(self):
        c1 = Contact('Ataw Wallpa', '801-993-9313', date(1502, 3, 30))
        c2 = Contact('Tupac Cusi', '(29) 45873-1571', date(1491, 4, 1))
        c3 = Contact('Huayna Capac', '(31) 1235-4212', date(1468, 3, 12))
        c4 = Contact('Ana', '(31) 4321-9876', date(1942, 12, 1))
        c5 = Contact('Ana', '(31) 6723-2132', date(1999, 3, 1))

        contact_list = ContactList([c1, c2, c3, c4, c5])

        actual_contacts = list(map(lambda x: x[1], contact_list.search_by_name('Ana')))
        expected_contacts = [c4, c5]
        self.assertEqual(actual_contacts, expected_contacts)

        actual_contacts = list(map(lambda x: x[1], contact_list.search_by_first_letter('a')))
        expected_contacts = [c1, c4, c5]
        self.assertEqual(actual_contacts, expected_contacts)

        actual_contacts = list(map(lambda x: x[1], contact_list.get_birthday_people(month=3)))
        expected_contacts = [c1, c3, c5]
        self.assertEqual(actual_contacts, expected_contacts)


if __name__ == '__main__':
    unittest.main()
