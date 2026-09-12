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


# Input
n, q = map(int, input().split())

queries = []
for _ in range(q):
    a, b, k = map(int, input().split())
    queries.append([a, b, k])

print(arrayManipulation(n, queries))