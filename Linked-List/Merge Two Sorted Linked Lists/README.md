# Merge Two Sorted Linked Lists

## Problem

Given the heads of two sorted singly linked lists, merge them into a single sorted linked list.

Either linked list can be empty (`null`).

### Example

**List A:**

```text
1 → 2 → 3
```

**List B:**

```text
3 → 4
```

**Merged List:**

```text
1 → 2 → 3 → 3 → 4
```

## Approach

1. Create a dummy node to simplify the merging process.
2. Compare the current nodes of both linked lists.
3. Attach the smaller node to the merged list.
4. Move the pointer of the selected list forward.
5. Continue until one list becomes empty.
6. Attach the remaining nodes from the other list.
7. Return the merged list.

## Python 3 Solution

```python
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

    if headA:
        current.next = headA
    else:
        current.next = headB

    return dummy.next
```

## Complexity

* **Time Complexity:** `O(n + m)`
* **Space Complexity:** `O(1)`

Where `n` and `m` are the lengths of the two linked lists.


