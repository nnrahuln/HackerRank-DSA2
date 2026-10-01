def getNode(head, positionFromTail):
    values = []

    current = head

    while current:
        values.append(current.data)
        current = current.next

    return values[len(values) - 1 - positionFromTail]