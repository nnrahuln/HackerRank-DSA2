# Insert a Node at the Tail of a Linked List

Part of the [MyCodeSchool](http://www.youtube.com/mycodeschool) linked list tutorial track.

## Problem

You're given the head of a singly linked list and an integer. Create a new
node containing that integer, attach it as the **last** node of the list,
and return the head of the resulting list.

* The head pointer may be `null` / `None`, meaning the list starts empty.
* You must return the head so the caller can access the full list — this
matters because if the list was empty, the head itself changes.

## Approach

1. Create the new node with `next` set to null.
2. If `head` is null, the new node **is** the list — return it directly.
3. Otherwise, walk from `head` until you find the node whose `next` is
null (the current tail).
4. Point that node's `next` at the new node.
5. Return the original `head` (unchanged, since we only appended).

**Complexity:** O(n) time (must walk to the end), O(1) extra space.
If you expect many insertions, keeping a separate tail pointer around
avoids the O(n) walk each time — but for this exercise, walking to the
tail is the expected solution.

## Files

|File|Language|
|-|-|
|`insert\\\_node\\\_at\\\_tail.c`|C|
|`insert\\\_node\\\_at\\\_tail.cpp`|C++|
|`Solution.java`|Java|
|`insert\\\_node\\\_at\\\_tail.py`|Python 3|

Each file is self-contained: it defines the node type, the
`insertNodeAtTail` function, and a small driver `main` that reads input
in the format below, builds the list by repeatedly inserting at the
tail, then prints each value on its own line.

## Input Format

```
n
value\\\_1
value\\\_2
...
value\\\_n
```

* `n` — number of values to insert, one after another, at the tail.
* Each following line is one integer to insert.

## Sample Input

```
5
141
302
164
530
474
```

## Sample Output

```
141
302
164
530
474
```

## How to Run

**C**

```bash
gcc insert\\\_node\\\_at\\\_tail.c -o insert\\\_node\\\_at\\\_tail
./insert\\\_node\\\_at\\\_tail < input.txt
```

**C++**

```bash
g++ insert\\\_node\\\_at\\\_tail.cpp -o insert\\\_node\\\_at\\\_tail
./insert\\\_node\\\_at\\\_tail < input.txt
```

**Java**

```bash
javac Solution.java
java Solution < input.txt
```

**Python 3**

```bash
python3 insert\\\_node\\\_at\\\_tail.py < input.txt
```

Where `input.txt` contains the sample input above (or your own test data).



