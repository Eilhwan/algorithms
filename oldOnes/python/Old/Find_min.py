def roll(query, table):
    min_val = table[query[0]][query[1]]
    temp = table[query[0]][query[1]]
    for i in range(query[1] + 1, query[3] + 1):
        col = query[0]
        table[col][i], temp = temp, table[col][i]
        min_val = min(min_val, temp)
    for i in range(query[0] + 1, query[2] + 1):
        row = query[3]
        temp, table[i][row] = table[i][row], temp
        min_val = min(min_val, temp)
    for i in range(query[3] - 1, query[1] - 1, -1):
        col = query[2]
        temp, table[col][i] = table[col][i], temp
        min_val = min(min_val, temp)
    for i in range(query[2] - 1, query[0] - 1, -1):
        row = query[1]
        temp, table[i][row] = table[i][row], temp
        min_val = min(min_val, temp)
    return min_val

def solution(rows, columns, queries):
    table = [[] for _ in range(columns + 1)]
    temp = 1
    for i in range(1, columns + 1):
        for j in range(1, rows + 1):
            table[i].append(temp)
            temp += 1

    answer = []
    for i in range(len(queries)):
        for j in range(len(table)):
            for k in range(len(table[j])):
                print(table[j][k], end="    ")
            print()
        answer.append(roll(queries[i], table))
    
    return answer

res = solution(6, 6, [[1, 1, 4, 5],[3, 3, 4, 5]])

print(res)