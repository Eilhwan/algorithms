# 6
# 9
# 1 2 5
# 1 3 4
# 2 3 2
# 2 4 7
# 3 4 6
# 3 5 11
# 4 5 3
# 4 6 8
# 5 6 8
import sys; input = sys.stdin.readline

def network(graph, m):
    parent = [i for i in range(m + 1)]

    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]
    
    def union(a, b):
        head_a = find(a)
        head_b = find(b)
        if head_a != head_b:
            if head_a > head_b:
                parent[head_a] = head_b
            else:
                parent[head_b] = head_a


    graph.sort(key=lambda x : x[2])
    value = 0
    for a, b, c in graph:
        if find(a) != find(b):
            union(a, b)
            value += c
    return value




n = int(input())
m = int(input())

graph = []
for _ in range(m):
    a, b, c = map(int, input().split()) # a to b c는 코스트
    graph.append([a, b, c])

print(network(graph, m))