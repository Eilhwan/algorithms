from collections import deque
import sys

m, n, h = map(int, sys.stdin.readline().split())
box = []
for _ in range(h):
    box1 = []
    for _ in range(n):
        box1.append(list(map(int, sys.stdin.readline().split())))
    box.append(box1)

que = deque()
for i in range(len(box)):
    for j in range(len(box[0])):
        for k in range(len(box[0][0])):
            if box[i][j][k] == 1:
                que.append([i, j, k])
print(que)