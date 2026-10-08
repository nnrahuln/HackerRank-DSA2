# 🔄 Detect a Cycle — Linked List

## 📌 Problem

A linked list contains a **cycle** if, while traversing the list, we visit the same node more than once.

Given the head of a singly linked list, determine whether the linked list contains a cycle.

* Return `1` if a cycle exists.
* Return `0` if there is no cycle.
* If the list is empty, return `0`.

---

## 💡 Approach

This solution uses **Floyd's Cycle Detection Algorithm**, also known as the **Tortoise and Hare Algorithm**.

We use two pointers:

* `slow` moves one node at a time.
* `fast` moves two nodes at a time.

If a cycle exists, `slow` and `fast` will eventually meet.

If `fast` reaches `None`, the linked list does not contain a cycle.

---

## 🧠 Algorithm

1. Initialize `slow` and `fast` with the head node.
2. Move `slow` one step.
3. Move `fast` two steps.
4. If `slow == fast`, a cycle exists → return `1`.
5. If `fast` or `fast.next` becomes `None`, there is no cycle → return `0`.

---

## 💻 Python Solution

```python
def has_cycle(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return 1

    return 0
```

---

## 📊 Complexity

| Complexity | Value  |
| ---------- | ------ |
| Time       | `O(n)` |
| Space      | `O(1)` |

The algorithm is efficient because it does not require extra memory to store visited nodes.

---

## 🔍 Example

### Without Cycle

```text
1 → 2 → 3 → 4 → None
```

Output:

```text
0
```

### With Cycle

```text
1 → 2 → 3 → 4
    ↑       ↓
    ← ← ← ←
```

Output:

```text
1
```

---

## 🚀 Key Concept

**Floyd's Cycle Detection Algorithm**

> If two pointers move at different speeds through a cyclic linked list, they will eventually meet.

---

## 🏆 Platform

**HackerRank — Detect a Cycle**

**Topic:** Linked List
**Difficulty:** Medium
**Language:** Python
