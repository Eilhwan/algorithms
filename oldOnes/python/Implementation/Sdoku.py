# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0

board = []
g = []
for _ in range(9):
    board.append(list(map(int, input().split())))

for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            g.append([i, j])


def recursive(g):
    if not g:
        return

    x, y = g.pop()
    dic = [{e: False for e in range(1, 10)} for _ in range(3)]

    for i in range(9):
        tmp = board[i][y]
        if tmp != 0:
            dic[0][tmp] = True

    for i in range(9):
        tmp = board[x][i]
        if tmp != 0:
            dic[1][tmp] = True

    for i in range(x // 3, x // 3 + 3):
        for j in range(y // 3, y // 3 + 3):
            tmp = board[i][j]
            if tmp != 0:
                dic[1][tmp] = True

    li = []

    for i in range(3):
        tmp = []
        for j in dic[i].keys():
            if not dic[i][j]:
                tmp.append(j)
        if not li:
            li = tmp
        else:
            if len(tmp) < len(li):
                li = tmp

    for i in range(len(li)):
        board[x][y] = li[i]
        recursive(g)


recursive(g)

print()
for i in range(9):
    for j in range(9):
        print(board[i][j], end=" ")
    print()
