def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

INF = int(10e9)

# 인접 행렬
graph =[
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

visited = [False * len(graph)]

dfs(graph, 0, visited)