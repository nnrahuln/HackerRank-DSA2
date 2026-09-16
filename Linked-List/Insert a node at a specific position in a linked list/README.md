# Insert a Node at a Specific Position

## Problem

Given the head of a singly linked list, an integer `data`, and a zero-based `position`, insert a new node containing `data` at the specified position.

Return the head of the updated linked list.

## Example

Original linked list:

```text
16 -> 13 -> 7
```

Insert `1` at position `2`:

```text
16 -> 13 -> 1 -> 7
```

## Approach

1. Create a new node with the given data.
2. If the position is `0`, insert the new node at the head.
3. Otherwise, move through the list until reaching the node before the required position.
4. Connect the new node to the next node.
5. Connect the previous node to the new node.
6. Return the head of the linked list.

## Function

```python
def insertNodeAtPosition(llist, data, position):
```

### Parameters

* `llist` – Head node of the singly linked list.
* `data` – Integer value to insert.
* `position` – Zero-based position where the new node should be inserted.

### Returns

* The head node of the revised linked list.

## Sample Input

```text
3
16
13
7
1
2
```

## Sample Output

```text
16 13 1 7
```

## Complexity

* **Time Complexity:** `O(n)` in the worst case
* **Space Complexity:** `O(1)` auxiliary space

## Platform

HackerRank – Data Structures – Linked Lists

## Language

Python
