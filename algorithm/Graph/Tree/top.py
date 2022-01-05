def dfs(start, graph):
    visit = [False for _ in range(len(graph))]
    st = [start]
    visit[start] = True
    res = 0
    while st:
        r = st.pop()
        res += 1
        
        for v in graph[r]:
            if v not in st and not visit[v]:
                visit[v] = True
                st.append(v)
    return res

def solution(n, wires):
    answer = 101
    for k in range(n - 1):
        temp = wires[:]
        a, b = temp.pop(k)
        graph = [[] for _ in range(n + 1)]
        for x, y in temp:
            graph[x].append(y)
            graph[y].append(x)
        
        answer = min(answer, abs(dfs(a, graph) - dfs(b, graph)))
        
        
    return answer

n = 9
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]	
print(solution(n, wires))


uf = []

def find(a):
    global uf
    if uf[a] < 0: return a
    uf[a] = find(uf[a])
    return uf[a]

def merge(a, b):
    global uf
    pa = find(a)
    pb = find(b)
    if pa == pb: return
    uf[pa] += uf[pb]
    uf[pb] = pa

def solution(n, wires):
    global uf
    answer = int(1e9)
    k = len(wires)
    for i in range(k):
        uf = [-1 for _ in range(n+1)]
        tmp = [wires[x] for x in range(k) if x != i]
        for a, b in tmp: merge(a, b)
        v = [x for x in uf[1:] if x < 0]
        answer = min(answer, abs(v[0]-v[1]))

    return answer