n, m = map(int, input().split())

mat = [list(map(int, input().split()))for _ in range(n)]
visited = [[False] * m for _ in range(n)]

max_value = 0
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

def dfs(x, y, _sum, cnt):
    global max_value
    if cnt == 4:
        max_value = max(max_value, _sum)
        return
        
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, _sum + mat[x][y], cnt + 1)
            visited[nx][ny] = False
            
def func(x, y):
    global max_value
    for i in range(4):
        value = mat[x][y]
        for j in range(3):
            t = (i + j) % 4
            nx = x + dx[t]
            ny = y + dy[t]
            if not (0 <= nx < n and 0 <= ny < m):
                value = 0
                break
            value += mat[nx][ny]
        max_value = max(max_value, value)

for i in range(n):
    for j in range(m):
        # 도형 하나씩 대보기
        visited[i][j] = True
        dfs(i, j, mat[i][j], 1)
        visited[i][j] = False
        func(i, j)

print(max_value)
        
