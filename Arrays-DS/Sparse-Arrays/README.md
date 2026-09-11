# Sparse Arrays - HackerRank

## Problem

Given a collection of strings and a collection of query strings, find how many times each query string occurs in the collection.

## Example

### Input

```text
4
aba
baba
aba
xzxb
3
aba
xzxb
ab
```

### Output

```text
2
1
0
```

## Explanation

The string `aba` occurs 2 times.

The string `xzxb` occurs 1 time.

The string `ab` does not occur in the list, so its count is 0.

## Approach

For every query:

1. Search for the query in `stringList`.
2. Count how many times it occurs.
3. Store the count in the result array.
4. Print each result.

Python's `count()` method is used to count the occurrences.

## Complexity

* Time Complexity: `O(n × q)` in the simple implementation.
* Space Complexity: `O(q)` for the result array.

## Language

Python 3

## Platform

HackerRank
