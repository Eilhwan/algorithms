INF = int(10e9)
n = 6
start = 1

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def daikstra(graph, start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    
    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True

        for j in graph[now]:
            cost = distance[now] + j[i]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
    return distance






distance = [INF] * (n + 1)
edge = [
    [1, 2, 2],
    [1, 3, 5],
    [1, 4, 1],
    [2, 3, 3],
    [2, 4, 2],
    [3, 2, 3],
    [3, 6, 5],
    [4, 3, 3],
    [4, 5, 1],
    [5, 3, 1],
    [5, 6, 2]
]

graph = [[] for _ in range(n + 1)]

for a, b, c in edge:
    graph[a].append((b, c))
visited = [False] * (n + 1)

print(daikstra(graph, 1))