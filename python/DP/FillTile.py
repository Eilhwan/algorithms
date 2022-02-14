
# 1 <= N <= 30
N = int(input())


dpTable = [1]

dpTable.append(0)
dpTable.append(3)
dpTable.append(0)
# += 2
for i in range(4, N+1):
    dpTable.append(dpTable[i-2] * 3)
    for j in range(4, i+1, 2):
        dpTable[i] += dpTable[i-j] * 2


print(dpTable)
