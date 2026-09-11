def reverseArray(a):
    return a[::-1]


n = int(input())
arr = list(map(int, input().split()))

result = reverseArray(arr)

print(*result)