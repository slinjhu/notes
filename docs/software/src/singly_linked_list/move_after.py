from .list_node import ListNode


def move_after(src, dest):
    if src and src.next and dest:
        to_move = src.next
        src.next = to_move.next
        to_move.next = dest.next
        dest.next = to_move