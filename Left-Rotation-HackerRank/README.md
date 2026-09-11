# Left Rotation

## Problem

Given an array, rotate the array to the left by `d` positions.

In a left rotation, the first element moves to the end of the array.

### Example

Input:

```text
5 4
1 2 3 4 5
```

After 4 left rotations:

```text
5 1 2 3 4
```

## Solution

The solution uses Python list slicing.

```python
def rotateLeft(d, arr):
    d = d % len(arr)
    return arr[d:] + arr[:d]
```

### Explanation

For:

```text
arr = [1, 2, 3, 4, 5]
d = 4
```

We divide the array into two parts:

```text
arr[d:] = [5]
arr[:d] = [1, 2, 3, 4]
```

Then combine them:

```text
[5] + [1, 2, 3, 4]
```

Result:

```text
[5, 1, 2, 3, 4]
```

## Complexity

* Time Complexity: `O(n)`
* Space Complexity: `O(n)`

## Language

Python 3

## Platform

HackerRank
