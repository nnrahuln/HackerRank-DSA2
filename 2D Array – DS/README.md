# HackerRank Array Problems – Python

This repository contains solutions for two HackerRank array problems implemented in **Python**.

## Problems

### 1. Reverse an Array

**Problem:** Arrays - DS

The task is to reverse an array of integers.

#### Example

Input:

```text
4
1 4 3 2
```

Output:

```text
2 3 4 1
```

#### Approach

Python provides a simple way to reverse an array using slicing:

```python
def reverseArray(a):
    return a[::-1]
```

#### Time Complexity

* **Time:** O(n)
* **Space:** O(n)

---

### 2. 2D Array – Hourglass Sum

**Problem:** 2D Array - DS

An hourglass consists of 7 elements arranged in this pattern:

```text
a b c
  d
e f g
```

For a 6 × 6 array, there are **16 possible hourglasses**.

The task is to calculate the sum of every hourglass and return the **maximum hourglass sum**.

#### Example

Input:

```text
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0
```

Output:

```text
19
```

#### Approach

For every possible starting position, calculate the 7 values belonging to the hourglass:

```python
def hourglassSum(arr):
    max_sum = -63

    for i in range(4):
        for j in range(4):
            total = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1]
                + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )

            max_sum = max(max_sum, total)

    return max_sum
```

#### Time Complexity

* **Time:** O(1) for the fixed 6 × 6 input
* **Space:** O(1)

---

## Technologies Used

* Python 3
* HackerRank
* Arrays
* 2D Arrays
* Loops
* Functions

## Concepts Practiced

* Array manipulation
* Array slicing
* 2D arrays
* Nested loops
* Indexing
* Maximum value calculation
* Time and space complexity

## HackerRank Problems

* **Arrays - DS**
* **2D Array - DS**

## Author

**Rahul N N**

BE – Artificial Intelligence & Machine Learning
Ghousia College of Engineering
