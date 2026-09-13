# Print Linked List - HackerRank

## Problem

Given the head of a linked list, print the data value of each node, one value per line.

## Example

Linked List:

```text
16 -> 13 -> NULL
```

Output:

```text
16
13
```

## Solution

The solution starts from the head node and traverses the linked list using the `next` pointer.

```python
def printLinkedList(head):
    current = head

    while current is not None:
        print(current.data)
        current = current.next
```

## Logic

1. Start from `head`.
2. Check whether the current node is `None`.
3. Print `current.data`.
4. Move to the next node using `current.next`.
5. Continue until the end of the linked list.

## Complexity

* Time Complexity: `O(n)`
* Space Complexity: `O(1)`

## Platform

HackerRank

## Language

Python
