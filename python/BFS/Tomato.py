from collections import deque

def bfs():
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < r and 0 <= y < c and box[x][y] == 0:
                box[x][y] = box[a][b] + 1
                q.append([x, y])

c, r = map(int, input().split())
box = []
q = deque()

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

for i in range(r):
    box.append(list(map(int, input().split())))

for i in range(r):
    for j in range(c):
        if box[i][j] == 1:
            q.append([i, j])

bfs()

is_prematured = False
res = -2

for col in box:
    for tomato in col:
        if tomato == 0:
            is_prematured = True
        res = max(res, tomato)

if is_prematured:
    print(-1)
elif res == -1:
    print(0)
else:
    print(res - 1)

