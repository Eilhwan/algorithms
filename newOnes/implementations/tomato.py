from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
box = []
queue = deque()

for i in range(h):
    box1 = []
    for j in range(n):
        box1.append(list(map(int, sys.stdin.readline().split())))
        for k in range(m):
            if box1[j][k] == 1:
                queue.append([i, j, k])
    box.append(box1)

dz = [0, 0, 0, 0, 1, -1]
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, -1, 0, 0, 0]
while queue:
    z, x, y = queue.popleft()
    
    for i in range(6):
        a = z+dz[i]
        b = x+dx[i]
        c = y+dy[i]
        if 0 <= a < h and 0 <= b < n and 0 <= c < m and box[a][b][c] == 0:
            queue.append([a,b,c])
            box[a][b][c] = box[z][x][y]+1
            
day = 0
for i in box:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)