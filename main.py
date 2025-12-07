class Node:
    """
    Simple singly linked list node.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def remove_cars(head, target):
    """
    Remove all nodes whose value == target from the list starting at head.
    Return the new head.
    """

    # 1. Remove matching nodes at the FRONT
    while head is not None and head.value == target:
        head = head.next

    # If the whole list is removed
    if head is None:
        return None

    # 2. Remove matching nodes in the MIDDLE
    prev = head
    curr = head.next

    while curr is not None:
        if curr.value == target:
            # Skip this node
            prev.next = curr.next
        else:
            # Move prev forward only when NOT removing
            prev = curr
        curr = curr.next

    return head
