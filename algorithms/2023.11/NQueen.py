def check(row):
    for i in range(row):
        if chessMap[i] == chessMap[row] or (row - i == abs(chessMap[row] - chessMap[i])):
            return False
    return True

def recursive(i):
    global answer
    if i == N:
        answer += 1
        return
    
    for j in range(N):
        chessMap[i] = j
        if check(i):
            recursive(i+1)

N = int(input())

chessMap = [-1 for _ in range(N)]
answer = 0

recursive(0)
print(answer)