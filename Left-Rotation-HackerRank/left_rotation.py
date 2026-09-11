def rotateLeft(d, arr):
    d = d % len(arr)
    return arr[d:] + arr[:d]


n, d = map(int, input().split())
arr = list(map(int, input().split()))

result = rotateLeft(d, arr)

print(*result)