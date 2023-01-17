import sys;input=sys.stdin.readline
from heapq import heappop, heappush
n = int(input()) # city
m = int(input()) # bus

INF = int(10e9)
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, d = map(int, input().split())

q = [(0, s)]
dist[s] = 0
while q:
    c, now = heappop(q)
    if dist[now] < c:
        continue
    for cost, vertex in graph[now]:
        c_plus = cost + c
        if c_plus < dist[vertex]:
            dist[vertex] = c_plus
            heappush(q, (c_plus, vertex))

print(dist[d])
