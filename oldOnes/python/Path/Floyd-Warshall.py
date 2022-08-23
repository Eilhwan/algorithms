# 5
# 9
# 1 2 4
# 1 3 5
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
# 3 5 1
INF = 10e9

# 노드의 개수와 간선의 개수
n = int(input())
m = int(input())
# 2차원 리스트
graph = [[INF if i != j else 0 for i in range(n + 1)] for j in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c


for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] != 10e9 else "INF", end="  ")
    print()


