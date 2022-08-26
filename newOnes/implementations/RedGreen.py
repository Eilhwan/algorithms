n = int(input())
matrix = [list(input().rstrip()) for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
ans = []

for _ in range(2):

    que = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                que.append([i, j])
                while que:
                    x, y = que.pop()
                    visited[x][y] = True
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if matrix[i][j] == matrix[nx][ny] and not visited[nx][ny]:
                                que.append([nx, ny])
                cnt += 1
    
    ans.append(cnt)

    for i in range(n):
        for j in range(n):
            if matrix[i][j] == "G":
                matrix[i][j] = "R"

print(ans[0], ans[1])