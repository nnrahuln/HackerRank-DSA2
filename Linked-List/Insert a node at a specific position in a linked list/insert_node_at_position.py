def insertNodeAtPosition(llist, data, position):
    new_node = SinglyLinkedListNode(data)

    # Insert at head
    if position == 0:
        new_node.next = llist
        return new_node

    current = llist

    # Move to the node before the required position
    for _ in range(position - 1):
        current = current.next

    # Insert the new node
    new_node.next = current.next
    current.next = new_node

    return llist