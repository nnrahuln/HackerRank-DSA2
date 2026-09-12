# Array Manipulation

## Problem

You are given an array of `n` elements initially containing zeros.

For each query:

```text
a b k
```

add `k` to every element from index `a` to index `b`, inclusive.

After processing all queries, return the **maximum value** in the array.

---

## Example

### Input

```text
5 3
1 2 100
2 5 100
3 4 100
```

### Operations

```text
1 2 100
2 5 100
3 4 100
```

The final array becomes:

```text
100 200 200 200 100
```

Therefore, the maximum value is:

```text
200
```

### Output

```text
200
```

---

## Approach

A direct approach would update every element between `a` and `b` for every query.

This can be slow when `n` and the number of queries are large.

Instead, we use a **Difference Array**.

For every query:

```text
a b k
```

we perform:

```python
arr[a] += k
arr[b + 1] -= k
```

After processing all queries, calculate the prefix sum.

The prefix sum represents the actual value at each index.

---

## Algorithm

1. Create an array of size `n + 2` initialized with zeros.
2. For every query `(a, b, k)`:

   * Add `k` at position `a`.
   * Subtract `k` at position `b + 1`.
3. Traverse the array from index `1` to `n`.
4. Maintain a running prefix sum.
5. Keep track of the maximum prefix sum.
6. Return the maximum value.

---

## Complexity

### Time Complexity

```text
O(n + q)
```

Where:

* `n` = array size
* `q` = number of queries

### Space Complexity

```text
O(n)
```

---

## Python Code

```python
def arrayManipulation(n, queries):
    arr = [0] * (n + 2)

    for a, b, k in queries:
        arr[a] += k
        arr[b + 1] -= k

    current = 0
    maximum = 0

    for i in range(1, n + 1):
        current += arr[i]
        maximum = max(maximum, current)

    return maximum


n, q = map(int, input().split())

queries = []

for _ in range(q):
    a, b, k = map(int, input().split())
    queries.append([a, b, k])

print(arrayManipulation(n, queries))
```

---

## Key Concept

The important concept used in this problem is:

**Difference Array + Prefix Sum**

Instead of modifying every element for every query, we record only where the addition starts and where it ends.

This makes the solution much faster for large inputs.

## HackerRank

Problem: **Array Manipulation**

Language: **Python 3**
