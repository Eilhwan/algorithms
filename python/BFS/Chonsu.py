import sys; read = sys.stdin.readline

def dfs(x, y):
    global visit
    visit[x] = 1
    st = [x]
    while st:
        r = st.pop()
        for i in graph[r]:
            if visit[i] == 0 and i not in st:
                visit[i] = visit[r] + 1
                st.append(i)


n = int(read())
a, b = map(int, read().split())
m = int(read())

graph = [[] for _ in range(n + 1)]
visit = [0] * (n + 1)
for i in range(m):
    x, y = map(int, read().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(a, b)
print(visit[b] - 1)
