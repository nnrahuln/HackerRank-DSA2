class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insertNodeAtTail(llist, data):
    new_node = SinglyLinkedListNode(data)

    if llist is None:
        return new_node

    current = llist

    while current.next is not None:
        current = current.next

    current.next = new_node

    return llist