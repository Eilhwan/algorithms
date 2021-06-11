n, m = map(int, input().split())
k = list(map(int, input().split()))
k = k[1:]

graph = [[] for _ in range(n + 1)]
arr = []
ans = 0

for i in range(m):
    invited = list(map(int, input().split()))
    invited = invited[1:]
    arr.append(invited)
    for i in range(len(invited)):
        for j in range(len(invited)):
            if invited[j] not in graph[invited[i]] and invited[i] != invited[j]:
                graph[invited[i]].append(invited[j])
for i in range(len(k)):
    # k = [1, 2, 3]
    for j in range(len(graph[k[i]])):
        # graph[2] = [1, 4]
        if graph[k[i]][j] not in k:
            k.append(graph[k[i]][j])
for i in range(len(arr)):
    for j in k:
        if j in arr[i]:
            ans += 1
            break
print(m - ans)