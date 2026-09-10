def dynamicArray(n, queries):
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]

        idx = (x ^ lastAnswer) % n

        if query_type == 1:
            arr[idx].append(y)

        elif query_type == 2:
            lastAnswer = arr[idx][y % len(arr[idx])]
            answers.append(lastAnswer)

    return answers


# Read input
n, q = map(int, input().split())

queries = []
for _ in range(q):
    queries.append(list(map(int, input().split())))

# Get answers
result = dynamicArray(n, queries)

# Print answers
for answer in result:
    print(answer)