# 3 3
# 1 2 1
# 2 3 2
# 1 3 3
def kruskal(graph):
    parent = [i for i in range(v+1)]
    level = [0 for _ in range(v+1)] # 가중치
    
    def find(x):
        if x != parent[x]:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a, b, c):
        head_a = find(a)
        head_b = find(b)
        if head_a != head_b:
            # parent가 다른 경우
            head = head_a if level[head_a] < head_b else head_b
            tail = head_a if level[head_a] > head_b else head_b
            
            parent[tail] = head
            level[head] += c

    for i in range(len(graph)):
        a, b, c = graph[i]
        if find(a) == find(b):
            return level[find(a)]
        union(a, b, c)

        

v, e = map(int, input().split())
graph = []

for _ in range(e):
    a, b, c = map(int, input().split()) # A to B C는 가중치
    graph.append([a, b, c])

print(kruskal(graph))
