def bfs():
    print(1)
def solution(m, n, board):
    items = set()
    dx = [0, 1, 1]
    dy = [1, 0, 1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            item = board[i][j]
            temp = []
            for k in range(3):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < len(board) and 0 <= ny < len(board):
                    if item != board[nx][ny]:
                        break
                    else:
                        temp.append(str(nx) + "," + str(ny))
            if len(temp) == 3:
                temp.append(str(i) + "," + str(j))
                items.update(temp)
    for i in items:
        x, y = map(int, i.split(","))
        board[x] = board[x][:y] + "X" + board[x][y + 1:]
            # 아래 
    print(board)
    print(items)

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
solution(m, n, board)