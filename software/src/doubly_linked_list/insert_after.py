from .list_node import ListNode


def insert_after(node, value):
    assert node is not None
    new_node = ListNode(value)
    new_node.previous = node
    new_node.next = node.next
    node.next.previous = new_node
    node.next = new_node
