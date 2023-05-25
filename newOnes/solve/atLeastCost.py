import sys;input=sys.stdin.readline
from heapq import heappop, heappush
n = int(input()) # city
m = int(input()) # bus

INF = int(10e9)
graph = [[] for _ in range(n+1)]
dist = [INF for _ in range(n+1)]
prev_node = [0 for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))

s, d = map(int, input().split())

q = [(0, s)]
dist[s] = 0
while q:
    c, now = heappop(q)
    if dist[now] < c:
        continue
    for cost, vertex in graph[now]:
        c_plus = cost + c
        if c_plus < dist[vertex]:
            dist[vertex] = c_plus
            prev_node[vertex] = now
            heappush(q, (c_plus, vertex))

print(dist[d])
path = [d]
now = d
while now != s:
    now = prev_node[now]
    path.append(now)
path.reverse()
print(len(path))
print(" ".join(map(str, path)))

# def dijkstra(s):
#     distance = [INF] * (N+1)
#     distance_path = [[] for _ in range(N+1)]
#     q = [[0, s, [s]]]
#     distance[s] = 0

#     while q:

#         now_cost, now_vertex, path = heapq.heappop(q)

#         for next_cost, next_vertex in Q[now_vertex]:
#             if next_cost + now_cost < distance[next_vertex]:
#                 next_cost += now_cost
#                 distance[next_vertex] = next_cost
#                 distance_path[next_vertex] = path + [next_vertex]
#                 heapq.heappush(q, [next_cost, next_vertex, path + [next_vertex]])

#     return distance, distance_path

# import sys, heapq
# INF = sys.maxsize

# N = int(input())
# M = int(input())
# Q = [[] for _ in range(N+1)]

# for _ in range(M):
#     start, end, cost = map(int, input().split())

#     Q[start].append([cost, end])

# S, E = map(int, input().split())
# answer, answer_path = dijkstra(S)

# print(answer[E])
# print(len(answer_path[E]))
# for element in answer_path[E]:
#     print(element, end = " ")