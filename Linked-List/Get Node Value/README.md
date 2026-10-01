# Get Node Value

## Problem

Given the head of a singly linked list and a position from the tail, find the data value of the node at that position.

The tail node is considered position `0`, the previous node is position `1`, and so on.

### Example

For the linked list:

```text
3 → 2 → 1
```

If `positionFromTail = 2`:

```text
Tail: 1 → position 0
      2 → position 1
      3 → position 2
```

So the answer is:

```text
3
```

## Function

Complete the following function:

```python
def getNode(head, positionFromTail):
```

### Parameters

* `head` — Pointer to the head of the singly linked list.
* `positionFromTail` — The position to retrieve, counting backwards from the tail.

### Returns

* `int` — The data value of the node at the specified position from the tail.

## Approach

1. Traverse the linked list and store the node values.
2. The position from the tail can be converted into an index from the beginning.
3. For a list of length `n`, the required index is:

```text
n - 1 - positionFromTail
```

4. Return the value at that index.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Sample Input

```text
2
1
1
0
3
3
2
1
2
```

## Sample Output

```text
1
3
```

## Topics
* Linked List
* Singly Linked List
* Traversal
* Data Structures
* HackerRank


