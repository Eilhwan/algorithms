from collections import deque

n, m, v = map(int, input().split())

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited):
    print()
    visited[v] = True
    q = deque([v])
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i] and i not in q:
                q.append(i)
                visited[i] = True

    

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for nodes in graph:
    nodes.sort()

visited = [False] * (n + 1)
dfs(graph, v, visited)
visited = [False] * (n + 1)
bfs(graph, v, visited)