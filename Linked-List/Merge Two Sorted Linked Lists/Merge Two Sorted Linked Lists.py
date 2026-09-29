def mergeLists(headA, headB):
    dummy = SinglyLinkedListNode(0)
    current = dummy

    while headA and headB:
        if headA.data <= headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next

        current = current.next

    # Attach remaining nodes
    if headA:
        current.next = headA
    else:
        current.next = headB

    return dummy.next