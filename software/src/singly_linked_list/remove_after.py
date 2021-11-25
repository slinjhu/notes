from .list_node import ListNode


def remove_after(node):
    if node and node.next:
        node.next = node.next.next
