def deleteNode(llist, position):
    # Delete the head node
    if position == 0:
        return llist.next

    current = llist

    # Move to the node before the node to delete
    for i in range(position - 1):
        current = current.next

    # Delete the node
    current.next = current.next.next

    return llist