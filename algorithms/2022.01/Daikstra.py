from heapq import heappop, heappush

n, m, x = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    s, v, w = map(int, input().split())
    graph[s].append((w, v))

def daikstra(start):
    dist = [int(10e9) for _ in range(len(graph))]
    s = (0, start)
    q = []
    dist[start] = 0
    heappush(q, s)
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

to_home = daikstra(x)
answer = 0
for i in range(1, n+1):
    to_x = daikstra(i)[x]
    answer = max(to_home[i] + to_x, answer)

print(answer)