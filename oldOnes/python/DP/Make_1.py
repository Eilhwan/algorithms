

n = int(input())

field = [0] * (n + 1)

for i in range(2, n + 1):
    field[i] = field[i - 1] + 1
    if i % 2 == 0:
        field[i] = min(field[i], field[i // 2] + 1)
    if i % 3 == 0:
        field[i] = min(field[i], field[i // 3] + 1)



print(field[n])