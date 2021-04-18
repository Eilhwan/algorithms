import sys; read = sys.stdin.readline
sys.setrecursionlimit(50 * 50)


def bfs(x, y):
    allie.append([x, y])
    visit[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if l <= abs(world[nx][ny] - world[x][y]) <= r and not visit[nx][ny]:
                bfs(nx, ny)


n, l, r = map(int, read().split())
world = []
dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]
for i in range(n):
    world.append(list(map(int, read().split())))

cnt = 0
is_true = True

while is_true:
    is_true = False
    allies = []
    visit = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            allie = []
            if not visit[i][j]:
                bfs(i, j)
            if len(allie) > 1:
                allies.append(allie)
    if len(allies) > 0: 
        is_true = True
        for al in allies:
            _sum = 0
            for x, y in al:
                _sum += world[x][y]
            avg = _sum // len(al)
            for x, y in al:
                world[x][y] = avg
    if is_true:
        cnt += 1

print(cnt)