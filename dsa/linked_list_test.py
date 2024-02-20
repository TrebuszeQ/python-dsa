import unittest

from linked_list import LinkedList


class LinkedListTestCase(unittest.TestCase):
    def setUp(self):
        self.linked_list = LinkedList()

    def test_node_valid(self):
        self.assertEqual(LinkedList.Node, self.linked_list.Node)

    def test_node_next(self):
        self.assertEqual(None, self.linked_list.Node.next)

    def test_linked_list_valid(self):
        self.assertEqual(type(self.linked_list), LinkedList)

    def test_insert_head_valid(self):
        linked_list = LinkedList()
        linked_list.insert_head("paczek")
        linked_list.insert_head("rurka")
        print(linked_list.__repr__())
        self.assertEqual("rurka", linked_list.head.data)
        self.assertEqual("paczek", linked_list.head.next.data)


if __name__ == '__main__':
    unittest.main()
