from collections import deque

n = 7

node = [
    [1, 2],
    [1, 4],
    [1, 5],
    [2, 5],
    [2, 6],
    [2, 7],
    [3, 4],
]


graph = [[] for _ in range(n + 1)]
visit = [False for _ in range(n + 1)]

for i in range(len(node)):
    a, b = node[i]
    graph[a].append(b)
    graph[b].append(a)

start = 1

q = deque()
q.append(start)

while q:
    v = q.popleft()
    visit[v] = True
    print(v, end=" ")
    for i in range(len(graph[v])):
        to = graph[v][i]
        if not visit[to] and to not in q:
            q.append(to)


