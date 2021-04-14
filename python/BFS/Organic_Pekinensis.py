from collections import deque
import datetime
import sys
read = sys.stdin.readline
def bfs(x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        field[x][y] = 2
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                q.append([nx, ny])
                

t = int(read())
start = datetime.datetime.now()
for i in range(t):
    n, m, k = map(int, read().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    data = []
    q = deque()
    cnt = 0
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(k):
        x, y = map(int, read().split())
        field[x][y] = 1
        data.append([x, y])

    for x, y in data:
        if field[x][y] == 1:
            cnt += 1
            bfs(x, y)
    print(cnt)
end = datetime.datetime.now()

print(end - start)