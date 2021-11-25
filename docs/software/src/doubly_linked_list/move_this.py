from .list_node import ListNode


def move_this(src: ListNode, dest: ListNode):
    """Move src to dest.next"""
    # Unlink src from the list
    src.previous.next = src.next
    src.next.previous = src.previous

    # Insert src after dest
    src.previous = dest
    src.next = dest.next
    dest.next.previous = src
    dest.next = src

