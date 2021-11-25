from .list_node import ListNode


def insert_after(node, value):
    assert node is not None
    new_node = ListNode(value)
    new_node.next = node.next
    node.next = new_node
    return new_node