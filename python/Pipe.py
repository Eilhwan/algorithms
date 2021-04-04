import sys

n = int(sys.stdin.readline())

home = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
for i in home:
    i.append(1)
home.append([1] * (n + 1))

pipe = [[0, 0], [0, 1]]
ans = 0

def move(pipe):
    global ans
    if pipe[1] == [n - 1, n - 1]:
        ans += 1
    # 벽에 닿을 경우
    elif pipe[1][0] > n - 1 or pipe[1][1] > n - 1 or home[pipe[1][0]][pipe[1][1]] == 1:
        ans += 0
    else:
        # 가로
        if pipe[0][0] == pipe[1][0]:
            if home[pipe[1][0]][pipe[1][1] + 1] != 1:
                move([[pipe[0][0], pipe[0][1] + 1], [pipe[1][0], pipe[1][1] + 1]])
            if home[pipe[1][0]][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1]] != 1:
                move([[pipe[0][0], pipe[0][1] + 1], [pipe[1][0] + 1, pipe[1][1] + 1]])
        # 세로
        elif pipe[0][1] == pipe[1][1]:
            if home[pipe[1][0] + 1][pipe[1][1]] != 1:
                move([[pipe[0][0] + 1, pipe[0][1]], [pipe[1][0] + 1, pipe[1][1]]])
            if home[pipe[1][0]][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1]] != 1:
                move([[pipe[0][0] + 1, pipe[0][1]], [pipe[1][0] + 1, pipe[1][1] + 1]])
        # 대각선
        elif pipe[0][0] == pipe[1][0] - 1 and pipe[0][1] == pipe[1][1] - 1:
            if home[pipe[1][0]][pipe[1][1] + 1] != 1:
                move([[pipe[0][0] + 1, pipe[0][1] + 1], [pipe[1][0], pipe[1][1] + 1]])
            if home[pipe[1][0] + 1][pipe[1][1]] != 1:
                move([[pipe[0][0] + 1, pipe[0][1] + 1], [pipe[1][0] + 1, pipe[1][1]]])
            if home[pipe[1][0]][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1] + 1] != 1 and home[pipe[1][0] + 1][pipe[1][1]] != 1:
                move([[pipe[0][0] + 1, pipe[0][1] + 1], [pipe[1][0] + 1, pipe[1][1] + 1]])
    
move(pipe)
print(ans)