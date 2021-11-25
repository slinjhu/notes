def remove_this(node):
    if node and node.previous:
        node.previous.next = node.next
    if node and node.next:
        node.next.previous = node.previous
