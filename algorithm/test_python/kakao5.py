from collections import deque

        
        

def solution(info, edges):
    graph = [[] for _ in range(len(info))]

    for s, e in edges:
        graph[s].append(e)
    
    start = 0
    sheep = 0
    wolves = 0
    visit = [0 for _ in range(len(info))]
    q = deque([start])

    while q:
        now = q.popleft()
        if info[now] == 0:
            sheep += 1
    
        elif info[now] == 1:
            wolves += 1
            
        if sheep <= wolves:
            break            
        
        for i in range(len(graph[now])):
            # 1, 8
            if info[graph[now][i]] == 0:    
                q.appendleft(graph[now][i])
            elif info[graph[now][i]] == 1:
                # endpoint
                if not graph[graph[now][i]]:
                    continue
                else:
                    q.append(graph[now][i])

        for i in range(len(q)):
            is_all_wolves = True
            if info[q[0]] == 0:
                break
            for j in range(len(graph[q[0]])):
                if info[graph[q[0]][j]] == 0:
                    is_all_wolves = False
                    break
            if is_all_wolves:
                q.append(q.popleft())
            else:
                break
        if is_all_wolves:
            for i in range(len(q)):
                if dfs(q[0], sheep, wolves, graph):
                    break
                else:
                    q.append(q.popleft())

            
    return sheep

def dfs(start, sheep, wolves, graph):
    global info
    
    if wolves >= sheep:
        return False
    if info[start] == 0:
        return True
    else:
        wolves += 1
    for i in range(len(graph[start])):
        dfs(graph[start][i], sheep, wolves, graph)
        wolves -= 1
    


edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]	
info = [0,1,0,1,1,0,1,0,0,1,0]

print(solution(info, edges))