def solution(m, n, board):
    ans = 0
    for i in range(len(board)):
        board[i] = list(board[i])
    dx = [0, 1, 1]
    dy = [1, 0, 1]

    while True:
        items = set()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "-":
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
            board[x][y] = "-"
        
        for i in range(len(board[0])):
            for j in range(len(board) - 1, -1, -1):
                if board[j][i] == "-":
                    for k in range(j - 1, -1, -1):
                        if board[k][i] != "-":
                            board[k][i], board[j][i] = board[j][i], board[k][i]
                            break
                    

        if len(items) == 0:
            break                
        else:
            ans += len(items)

    return ans

m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
print(solution(m, n, board))