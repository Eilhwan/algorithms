

graph = []
distance = [int(10e9) for _ in range(len(graph))]
visited = [False for _ in range(len(graph))]

def findMin():
    min_value = int(10e9)
    index = -1

    for i in range(len(distance)):
        if distance[i] < min_value and not visited[i]:
            index = i
            min_value = distance[i]
    
    return index

def daikstra(start):

    visited[start] = True
    distance[start] = 0

    for v in range(len(graph[start])):
        distance[v] = min(distance[v], graph[start][v])
    
    for i in range(len(distance) - 1):
        node = findMin()
        visited[node] = True

        for j in range(len(graph[i])):
            cost = graph[i][j]
            distance[j] = min(distance[j], distance[i] + cost)
            

daikstra(start=0)