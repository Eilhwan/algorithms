from heapq import heappush, heappop
from collections import deque

N, M, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
dist = [int(10e9)] * (N + 1)
visited = [False for _ in range(N + 1)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([w, v])

q = deque([0])

while q:
    now = q.popleft()
    for i in range(len(graph[now])):
        w, v = graph[now][i]
        dist[v] = min(dist[v], dist[now] + w)
        if not visited[v]:
            q.append(v)

print(dist)

result = 0

print(max(dist))
