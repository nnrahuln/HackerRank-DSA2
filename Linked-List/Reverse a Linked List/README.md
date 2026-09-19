# Reverse a Linked List

## Problem

Given the head node of a singly linked list, reverse the linked list by changing the `next` pointers of the nodes.

Return the head of the reversed linked list.

## Example

### Input

```text
1 → 2 → 3 → 4 → 5
```

### Output

```text
5 → 4 → 3 → 2 → 1
```

## Approach

We use three pointers:

* `previous` – stores the previous node.
* `current` – stores the current node.
* `next_node` – temporarily stores the next node.

For every node:

1. Store the next node.
2. Change `current.next` to point to `previous`.
3. Move `previous` to `current`.
4. Move `current` to `next_node`.

At the end, `previous` becomes the new head.

## Python Code

```python
def reverse(head):
    previous = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = previous
        previous = current
        current = next_node

    return previous
```

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)
* * **Time Complexity:** `O(n)``

Where `n` is the number of nodes in the linked list.

## HackerRank

Problem: **Reverse a linked list**

Topic: **Linked List**

Language: **Python 3**
