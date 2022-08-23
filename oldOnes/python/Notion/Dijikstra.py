import heapq

graph = [
    [],
    [(2, 2), (1, 3), (10, 5)],
    [(2, 4), (1, 5)],
    [(5, 4), (5, 5)],
    [(1, 6), (3, 7)],
    [(1, 7)],
    [],
    [(1, 6)]
]

distance = [10e9 for _ in range(len(graph))]

def dijkstra(start):
    que = []
    distance[start] = 0
    heapq.heappush(que, (0, start))

    while que:
        dist, now = heapq.heappop(que)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            d, to = i
            cost = distance[now] + d
            if distance[to] > cost:
                distance[to] = cost
                heapq.heappush(que, (cost, to))


dijkstra(1)
print(distance[1:])
