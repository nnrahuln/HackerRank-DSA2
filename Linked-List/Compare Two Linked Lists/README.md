# Compare Two Linked Lists

## Problem

You are given the head nodes of two singly linked lists.

Compare the data in both linked lists.

Return:

* `1` if both linked lists contain the same data in the same order and have the same length.
* `0` if the data is different or the lists have different lengths.

## Example

### List 1

```text
1 -> 2 -> NULL
```

### List 2

```text
1 -> 2 -> NULL
```

Output:

```text
1
```

### Another Example

List 1:

```text
1 -> 2 -> NULL
```

List 2:

```text
1 -> NULL
```

Output:

```text
0
```

The first node is equal, but the second list is shorter.

## Approach

1. Start from the head of both linked lists.
2. Compare the data of the current nodes.
3. If the data is different, return `0`.
4. Move both pointers to their next nodes.
5. Continue until one or both lists reach `NULL`.
6. If both lists reach `NULL` at the same time, return `1`.
7. If only one list reaches `NULL`, the lists have different lengths, so return `0`.

## Python Code

```python
def compare_lists(llist1, llist2):
    while llist1 is not None and llist2 is not None:
        if llist1.data != llist2.data:
            return 0

        llist1 = llist1.next
        llist2 = llist2.next

    if llist1 is None and llist2 is None:
        return 1

    return 0
```
Time Complexity

O(n)

Where n is the number of nodes checked.

Space Complexity

O(1)

No extra data structure is used.

###HackerRank###
