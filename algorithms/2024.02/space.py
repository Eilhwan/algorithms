import sys; input=sys.stdin.readline

# 5 7 3
# 0 2 4 4
# 1 1 2 5
# 4 0 6 2

m, n, k = map(int, input().split())

mat = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            mat[i][j] = 1

nx = [1, 0, 0, -1]
ny = [0, 1, -1, 0]

answer = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 0 and not visited[i][j]:
            stack = [[i, j]]
            cnt = 0
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                cnt += 1

                for ii in range(4):
                    dx = x + nx[ii]
                    dy = y + ny[ii]
                    if 0 <= dx < n and 0 <= dy < m:
                        if mat[dx][dy] == 0 and not visited[dx][dy]:
                            stack.append([dx, dy])
                            visited[dx][dy] = True
            answer.append(cnt)

print(len(answer))
print(" ".join(map(str, sorted(answer))))
                        


