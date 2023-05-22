from heapq import heappop, heappush

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
INF = int(10e9)
a = 100_000_000
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((c, b)) # c weight b vertex
v1, v2 = map(int, input().split())


# 1 -> v1
def dikstra(start):
    dist = [INF for _ in range(n+1)]
    q = []
    heappush(q, (0, start))
    dist[start] = 0
    while q:
        w, v = heappop(q)
        if dist[v] < w:
            continue

        for weight, vertex in graph[v]:
            cost = weight + w
            if cost < dist[vertex]:
                dist[vertex] = cost
                heappush(q, (cost, vertex))
    return dist
_1 = dikstra(1)
_v1 = dikstra(v1)
_v2 = dikstra(v2)

_1toV1 = _1[v1]
_1toV2 = _1[v2]
# v1 -> v2
v1toV2 = _v1[v2]
v2toV1 = _v2[v1]
# v2 -> n
v2toN = _v2[n]
v1toN = _v1[n]

cnt = min(_1toV1 + v1toV2 + v2toN, _1toV2 + v2toV1 + v1toN)
print(cnt if cnt < INF else -1)