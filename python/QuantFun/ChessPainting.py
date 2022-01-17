N, M = map(int, input().split())
arr = []
count = []

for _ in range(N):
    arr.append(input())

for i in range(N - 7):
    for j in range(M - 7):
        countW = 0
        countB = 0
        for w in range(i, i+8):
            for b in range(j, j+8):
                if (w+b) % 2 == 0:
                    if arr[w][b] != 'W':
                        countW += 1
                    if arr[w][b] != 'B':
                        countB += 1
                else:
                    if arr[w][b] != 'B':
                        countW += 1
                    if arr[w][b] != 'W':
                        countB += 1
        count.append(min(countW, countB))

print(min(count))
