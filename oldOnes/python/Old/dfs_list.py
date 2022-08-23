
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

edges = [
    [0, 1, 7],
    [0, 2, 5],
    [1, 0, 7],
    [2, 0, 5]
]

graph = [[] for _ in range(3)]

for edge in edges:
    graph[edge[0]].append([edge[1], edge[2]])


visited = [False * len(graph)]

dfs(graph, 0, visited)