def find_cycle(n, m, points):
    parent = [i for i in range(n)]  # 초기 부모 노드 설정
    rank = [0] * n  # 노드의 랭크 (트리의 높이)

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                if rank[root_x] == rank[root_y]:
                    rank[root_x] += 1
    for i in range(m):
        a, b = points[i]
        if find(a) == find(b):
            return i + 1
        union(a, b)
    return 0

n, m = map(int, input().split())

points = []
for _ in range(m):
    x, y = map(int, input().split())
    points.append([x, y])

print(find_cycle(n, m, points))
