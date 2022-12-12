import sys; input = sys.stdin.readline
from heapq import heapify, heappop, heappush

v, e = map(int, input().split())
k = int(input())

graph = [[] for _ in range(v+1)]
distance = [int(10e9) for _ in range(v+1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))

distance[k] = 0
li = []
heappush(li, (0, k))

while li:
    w, now = heappop(li)

    if distance[now] < w:
        continue

    for weight, to in graph[now]:
        if distance[now] + weight < distance[to]:
            distance[to] = distance[now] + weight
            heappush(li, (weight+w, to))
        

for i in range(1, len(distance)):
    if distance[i] == int(10e9):
        print("INF")
    else:
        print(distance[i])