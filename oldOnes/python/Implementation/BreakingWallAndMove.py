import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())
li = list()
visit = [[0 for _ in range(M)] for _ in range(N)]
ans = 10e9

for _ in range(N):
    li.append(list(input()))

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def backtracking(point, now, canBreakWall, visit):
    global ans
    x, y = point

    if x == N - 1 and y == M - 1:
        ans = min(ans, now)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if li[nx][ny] == "0" and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                backtracking([nx, ny], now + 1, canBreakWall, visit)
                visit[nx][ny] = 0
            elif canBreakWall and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                backtracking([nx, ny], now + 1, False, visit)
                visit[nx][ny] = 0
                canBreakWall = True


visit[0][0] = 1
backtracking([0, 0], 1, True, visit)

if ans == 10e9:
    print(-1)
else:
    print(ans)


# 6 6
# 000000
# 111110
# 000010
# 011000
# 011111
# 000000
