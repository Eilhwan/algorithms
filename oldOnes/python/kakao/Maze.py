import sys; sys.setrecursionlimit(10000000)

def dfs(i, end, graph, answer):
    if i == end:
        return answer
    if i in traps:
        trap(graph)
    for j in range(len(graph[i])):
        if graph[i][j] != 0:
            answer += graph[i][j]
            answer += dfs(j, end, graph, answer)
    return 0


def trap(graph):
    for i in range(len(graph)):
        for j in range(i, len(graph[i])):
            if j != i:
                graph[i][j], graph[j][i] = graph[j][i], graph[i][j]


def solution(n, start, end, roads, traps):
    graph = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(len(roads)):
        fr, to, dist = roads[i]
        graph[fr][to] = dist
    
    answer = 0
    
    dfs(start, end, graph, answer)
    
        


    return answer

n = 4
start =	1
end = 4
roads = [[1, 2, 1], [3, 2, 1], [2, 4, 1]]	
traps = [2, 3]	

print(solution(n, start, end, roads, traps))
# 4