def reversePrint(head):
    values = []

    current = head

    # Store all node values
    while current:
        values.append(current.data)
        current = current.next

    # Print in reverse order
    for value in reversed(values):
        print(value)