def solution(board, skill):
    answer = 0
    psum = [[0 for _ in range(len(board[0])+1)] for _ in range(len(board)+1)]

    for i in range(len(skill)):
        t, r1, c1, r2, c2, degree = skill[i]
        if t == 1:
            degree = -degree
        psum[r1][c1] += degree
        psum[r1][c2+1] -= degree
        psum[r2+1][c1] -= degree
        psum[r2+1][c2+1] += degree

    for i in range(len(psum) - 1):
        for j in range(len(psum[0]) - 1):
            psum[i][j + 1] += psum[i][j]

    for j in range(len(psum[0]) - 1):
        for i in range(len(psum) - 1):
            psum[i + 1][j] += psum[i][j]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += psum[i][j]
            if board[i][j] > 0:
                answer += 1
    # print(board)
    # print(psum)
    return answer
