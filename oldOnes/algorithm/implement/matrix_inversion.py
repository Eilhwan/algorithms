
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()


# for i in range(len(matrix)//2):
#     for j in range(len(matrix[0])):
#         matrix[i][j], matrix[len(matrix) - 1 - i][len(matrix[0]) - 1 - j] = matrix[len(matrix) - 1 - i][len(matrix[0]) - 1 - j], matrix[i][j]
for i in range(len(matrix)//2):
    for j in range(len(matrix[0]) - 1, -1, -1):
        matrix[i][j], matrix[len(matrix[0]) - 1 - j][len(matrix) - 1 - i] = matrix[len(matrix[0]) - 1 - j][len(matrix) - 1 - i], matrix[i][j]
print()
for i in range(len(matrix)):
    for j in range(len(matrix)):
        print(matrix[i][j], end=" ")
    print()
