def matchingStrings(stringList, queries):
    result = []

    for query in queries:
        count = stringList.count(query)
        result.append(count)

    return result


n = int(input())

stringList = []
for _ in range(n):
    stringList.append(input().strip())

q = int(input())

queries = []
for _ in range(q):
    queries.append(input().strip())

result = matchingStrings(stringList, queries)

for count in result:
    print(count)