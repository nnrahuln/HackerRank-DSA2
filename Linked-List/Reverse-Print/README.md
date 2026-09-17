# Reverse Print

## Problem

Given the head of a singly linked list, print all the node values in reverse order.

If the linked list is empty, print nothing.

## Example

Original linked list:

```text
1 → 2 → 3
```

Reverse order:

```text
3
2
1
```

## Approach

We cannot move backward in a singly linked list.

So:

1. Start from the head.
2. Store each node's data in a list.
3. Traverse until the end of the linked list.
4. Print the stored values in reverse order.

## Code

```python
def reversePrint(head):
    values = []

    current = head

    while current:
        values.append(current.data)
        current = current.next

    for value in reversed(values):
        print(value)
```

## Example

For:

```text
16 → 12 → 4 → 2 → 5
```

The stored list is:

```text
[16, 12, 4, 2, 5]
```

After reversing:

```text
5
2
4
12
16
```

## Complexity

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Key Concept

A singly linked list only moves forward.

```text
head
 ↓
16 → 12 → 4 → 2 → 5 → None
```

Therefore, we store the values first and then print them from the last value to the first value.
