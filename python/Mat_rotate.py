def rotate(x1, y1, x2, y2, matrix):
    temp = matrix[x1][y1]
    min_val = temp
    for i in range(1, y2 - y1 + 1):
        temp, matrix[x1][y1 + i] = matrix[x1][y1 + i], temp
        min_val = min(temp, min_val)
    
    for i in range(1, x2 - x1 + 1):
        temp, matrix[x1 + i][y2] = matrix[x1 + i][y2], temp
        min_val = min(temp, min_val)
    
    for i in range(1, y2 - y1 + 1):
        temp, matrix[x2][y2 - i] = matrix[x2][y2 - i], temp
        min_val = min(temp, min_val)
        
    for i in range(1, x2 - x1 + 1):
        temp, matrix[x2 - i][y1] = matrix[x2 - i][y1], temp
        min_val = min(temp, min_val)
    
    return min_val

def solution(rows, columns, queries):
    answer = []
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(1, columns + 1):
            matrix[i].append(i * columns + j)
    
    # 이 부분에 로직을 작성
    for c1, r1, c2, r2 in queries:
        answer.append(rotate(c1 - 1, r1 - 1, c2 - 1, r2 - 1, matrix))
    return answer

rows = 3	
cols = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 6
# cols = 6
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]

print(solution(rows, cols, queries))