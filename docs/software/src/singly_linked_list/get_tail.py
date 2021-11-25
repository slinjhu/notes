def get_tail(head):
    pt = head
    while pt and pt.next:
        pt = pt.next
    return pt
