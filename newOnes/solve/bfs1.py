from collections import deque

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]

    
# edges = [[0, 0, 0], [0, 0, 0], [1, 0, 0]]
edges = [[1, 1], [1, 1]]
tmpQue = deque([])
answer = -1
for i in range(len(edges)):
    for j in range(len(edges)):
        if edges[i][j] == 1:
            tmpQue.append([i, j])

while tmpQue:
    queue = tmpQue.copy()
    tmpQue = deque()
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(edges) and 0 <= ny < len(edges[0]):
                if edges[nx][ny] == 0:
                    tmpQue.append([nx, ny])
                    edges[nx][ny] = 1
    answer += 1
                    

print(answer)