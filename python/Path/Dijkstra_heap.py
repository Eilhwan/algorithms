# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
import heapq
import sys; read = sys.stdin.readline

INF = 10e9

# 노드의 개수, 간선의 개수
n, m = map(int, input().split())
# 시작 노드
start = int(input())
# 노드의 그래프
graph = [[] for _ in range(n + 1)]
# 방문 리스트
visited = [False for _ in range(n + 1)]
# 노드 to 노드 distance
distance = [INF for _ in range(n + 1)]

# 간선 정보
for _ in range(m):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        cost, node_num = heapq.heappop(q)
        if distance[node_num] < cost:
            continue
        for index, dist in graph[node_num]:
            if distance[index] > cost + dist:
                distance[index] = cost + dist
                heapq.heappush(q, (distance[index], index))
    return distance

print(dijkstra(start))                
