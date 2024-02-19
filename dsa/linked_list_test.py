import unittest

from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def test_linked_list(self):
        linked_list = LinkedList(None)
        self.assertEqual(type(linked_list), LinkedList)

    def test_insert_head(self):
        linked_list = LinkedList("paczek")
        linked_list.insert_head("rurka")
        print(linked_list.head.next)
        self.assertEqual("paczek", linked_list.head)


if __name__ == '__main__':
    unittest.main()
