def solution(board, skill):
    answer = 0
    
    for s in skill:
        t, r1, c1, r2, c2, d = s
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                if t == 1:
                    if board[i][j] > 0 and board[i][j] - d <= 0:
                        answer += 1
                    board[i][j] -= d

                else:
                    if board[i][j] <= 0 and board[i][j] + d > 0:
                        answer -= 1
                    board[i][j] += d
    

    return len(board) * len(board[i]) - answer

board = [[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]]	
skill = [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]]
print(solution(board, skill))
# skill의 각 행은 [type, r1, c1, r2, c2, degree]형태를 가지고 있습니다.
# type이 1일 경우는 적의 공격을 의미합니다. 건물의 내구도를 낮춥니다.
# type이 2일 경우는 아군의 회복 스킬을 의미합니다. 건물의 내구도를 높입니다.