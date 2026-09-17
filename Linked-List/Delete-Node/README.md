# Delete a Node

## Problem

Given a singly linked list and a position, delete the node at that position and return the head of the modified linked list.

The head node is at position `0`.

## Example

### Input

```text
8
20
6
2
19
7
4
15
9
3
```

Position to delete:

```text
3
```

Original list:

```text
20 → 6 → 2 → 19 → 7 → 4 → 15 → 9
```

After deleting position `3`:

```text
20 → 6 → 2 → 7 → 4 → 15 → 9
```

## Approach

### Case 1: Delete the first node

If `position == 0`, return the second node.

```python
return llist.next
```

### Case 2: Delete any other node

Move to the node just before the node that needs to be deleted.

Then skip the node:

```python
current.next = current.next.next
```

Finally, return the original head.

## Code

```python
def deleteNode(llist, position):
    if position == 0:
        return llist.next

    current = llist

    for _ in range(position - 1):
        current = current.next

    current.next = current.next.next

    return llist
```

## Time Complexity

* **Time:** `O(n)`
* **Space:** `O(1)`

## Key Concept

To delete a node in a singly linked list, we don't directly remove the node.

We make the previous node point to the node after it:

```text
Before:

10 → 20 → 30 → 40

Delete 30

After:

10 → 20 ─────→ 40
```

The important line is:

```python
current.next = current.next.next
```
