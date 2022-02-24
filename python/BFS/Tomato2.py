from collections import deque

# 5 3 1
# 0 -1 0 0 0
# -1 -1 0 1 1
# 0 0 0 1 1

# 첫 줄에는 상자의 크기를 나타내는 두 정수 M,N과 쌓아올려지는 상자의 수를 나타내는 H가 주어진다.
# M은 상자의 가로 칸의 수, N은 상자의 세로 칸의 수를 나타낸다.
# 단, 2 ≤ M ≤ 100, 2 ≤ N ≤ 100, 1 ≤ H ≤ 100 이다.
# 둘째 줄부터는 가장 밑의 상자부터 가장 위의 상자까지에 저장된 토마토들의 정보가 주어진다.
# 즉, 둘째 줄부터 N개의 줄에는 하나의 상자에 담긴 토마토의 정보가 주어진다.
# 각 줄에는 상자 가로줄에 들어있는 토마토들의 상태가 M개의 정수로 주어진다.
# 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토,
# 정수 -1은 토마토가 들어있지 않은 칸을 나타낸다.
# 이러한 N개의 줄이 H번 반복하여 주어진다.

# 토마토가 하나 이상 있는 경우만 입력으로 주어진다.

N, M, H = map(int, input().split())

box = []
visit = [[[False for _ in range(N)] for _ in range(M)] for _ in range(H)]

for J in range(H):
    face = []
    for _ in range(M):
        line = list(map(int, input().split()))
        face.append(line)

    box.append(face)

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

q = deque([[0, 0, 0]])
ans = 0

while q:
    day = False
    now = q.popleft()
    z, x, y = now[0], now[1], now[2]

    if z + 1 < H:
        temp = box[z][x][y]
        if (temp == 0 or temp == 1) and not visit[z][x][y]:
            q.append([z + 1, x, y])
            visit[z][x][y] = True
            box[z][x][y] = 1
            if not day:
                day = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N:
            temp = box[z][nx][ny]
            if (temp == 0 or temp == 1) and not box[z][nx][ny]:
                q.append([z, nx, ny])
                visit[z][nx][ny] = True
                box[z][nx][ny] = 1
                if not day:
                    day = True
    if day:
        ans += 1

if not day and ans == 0:
    print(-1)
else:
    print(ans)
