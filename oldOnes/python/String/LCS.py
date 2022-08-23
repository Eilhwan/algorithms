

a = input()
b = input()

table = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
answer = 0
for i in range(1, len(table)):
    for j in range(1, len(table[0])):
        if a[i-1] == b[j-1]:
            table[i][j] = table[i-1][j-1] + 1
            answer = max(table[i][j], answer)

print(answer)
