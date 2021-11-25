import unittest

from .list_node import ListNode
from .move_this import move_this
from .remove_this import remove_this
from .insert_after import insert_after


class TestDoubleLinkedList(unittest.TestCase):
    @staticmethod
    def make_list(size) -> ListNode:
        dummy_head = ListNode()
        pt = dummy_head
        for x in range(size):
            nd = ListNode(x)
            nd.previous = pt
            pt.next = nd
            pt = nd
        dummy_tail = ListNode()
        pt.next = dummy_tail
        dummy_tail.previous = pt
        return dummy_head

    def assertValue(self, node, str_value):
        pt = node
        values_next = []
        tail = None
        while pt is not None:
            values_next.append(str(pt.value))
            if pt.next is None:
                tail = pt
            pt = pt.next

        values_previous = []
        pt = tail
        while pt is not None:
            values_previous.append(str(pt.value))
            pt = pt.previous

        values_previous.reverse()
        self.assertListEqual(values_next, values_previous)
        self.assertEqual(' <=> '.join(values_next), str_value)

    def test_value(self):
        self.assertValue(None, '')
        self.assertValue(ListNode(5), '5')
        self.assertValue(self.make_list(2), 'None <=> 0 <=> 1 <=> None')

    def test_remove_tail(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')
        remove_this(dummy.next.next)
        self.assertValue(dummy, 'None <=> 0 <=> None')
        remove_this(dummy.next)
        self.assertValue(dummy, 'None <=> None')

    def test_remove_node(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')
        remove_this(dummy.next)
        self.assertValue(dummy, 'None <=> 1 <=> None')

    def test_insert(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')
        insert_after(dummy, 5)
        self.assertValue(dummy, 'None <=> 5 <=> 0 <=> 1 <=> None')

        dummy = self.make_list(0)
        self.assertValue(dummy, 'None <=> None')
        insert_after(dummy, 5)
        self.assertValue(dummy, 'None <=> 5 <=> None')

    def test_move_same(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')
        move_this(dummy.next, dummy)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')

    def test_move_tail(self):
        dummy = self.make_list(2)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> None')
        move_this(dummy.next.next, dummy)
        self.assertValue(dummy, 'None <=> 1 <=> 0 <=> None')

    def test_move_node(self):
        dummy = self.make_list(3)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> 2 <=> None')
        move_this(dummy.next.next, dummy)
        self.assertValue(dummy, 'None <=> 1 <=> 0 <=> 2 <=> None')

    def test_move_to_tail(self):
        dummy = self.make_list(3)
        self.assertValue(dummy, 'None <=> 0 <=> 1 <=> 2 <=> None')
        move_this(dummy.next, dummy.next.next.next)
        self.assertValue(dummy, 'None <=> 1 <=> 2 <=> 0 <=> None')


if __name__ == '__main__':
    unittest.main()
