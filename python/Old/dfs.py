

def dfs(grpah, start, visited):
    st = [start]

    while(st):
        v = st.pop()
        visited[v] = True
        print(v, end=" ")
        for i in grpah[v]:
            if not visited[i] and i not in st:
                st.append(i)


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

dfs(graph, 1, visited)