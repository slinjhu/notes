import unittest

from .list_node import ListNode
from .remove_after import remove_after
from .insert_after import insert_after
from .move_after import move_after
from .get_tail import get_tail


class TestLinkedList(unittest.TestCase):
    def assertValue(self, node, str_value):
        pt = node
        values = []
        while pt is not None:
            values.append(str(pt.value))
            pt = pt.next
        self.assertEqual('-> '.join(values), str_value)

    @staticmethod
    def make_list(size) -> ListNode:
        dummy = ListNode()
        pt = dummy
        for x in range(size):
            node = ListNode(x)
            pt.next = node
            pt = pt.next
        return dummy

    def test_value(self):
        self.assertValue(None, '')
        self.assertValue(ListNode(), 'None')
        self.assertValue(ListNode(5), '5')
        self.assertValue(self.make_list(2), 'None-> 0-> 1')

    def test_remove(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None-> 0-> 1')
        remove_after(dummy)
        self.assertValue(dummy, 'None-> 1')
        remove_after(dummy)
        self.assertValue(dummy, 'None')

        remove_after(None)
        remove_after(ListNode())

    def test_insert(self):
        dummy = self.make_list(0)
        self.assertValue(dummy, 'None')
        insert_after(dummy, 5)
        self.assertValue(dummy, 'None-> 5')
        insert_after(dummy, 2)
        self.assertValue(dummy, 'None-> 2-> 5')

    def test_move_with_same_src_dest(self):
        dummy = self.make_list(3)
        self.assertValue(dummy, 'None-> 0-> 1-> 2')
        move_after(dummy, dummy)
        self.assertValue(dummy, 'None-> 0-> 1-> 2')

    def test_move_to_tail(self):
        dummy = self.make_list(3)
        self.assertValue(dummy, 'None-> 0-> 1-> 2')
        tail = dummy
        while tail.next is not None:
            tail = tail.next
        move_after(dummy, tail)
        self.assertValue(dummy, 'None-> 1-> 2-> 0')

    def test_get_tail(self):
        dummy = self.make_list(3)
        tail = get_tail(dummy)
        self.assertEqual(tail.value, 2)
        self.assertIsNone(tail.next)

        self.assertIsNone(get_tail(None))

        self.assertEqual(get_tail(ListNode(5)).value, 5)


if __name__ == '__main__':
    unittest.main()


