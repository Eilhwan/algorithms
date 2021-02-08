from collections import deque


def bfs(graph, start, visited):
    que = deque([start])

    while que:
        v = que.popleft()
        visited[v] = True
        print(v, end=" ")
        for i in graph[v]:
            if not visited[i] and i not in que:
                que.append(i)

graph = [
    [],
    [2, 3, 4, 6],
    [1, 4],
    [1, 5],
    [1, 2, 5],
    [3, 4],
    [1]
]

visited = [False] * 7
visited[0] = True

bfs(graph, 1, visited)
    