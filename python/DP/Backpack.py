import sys
read = sys.stdin.readline

# N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
N, K = map(int, read().rstrip().split())

# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
things = []
for i in range(N):
    W, V = map(int, read().rstrip().split())
    things.append([W, V])
things.sort(key=lambda x: x[0])

matrix = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    weight = things[i-1][0]
    value = things[i-1][1]
    for j in range(1, K+1):
        if weight <= j:
            matrix[i][j] = max(matrix[i-1][j], matrix[i-1][j-weight] + value)
        else:
            matrix[i][j] = matrix[i-1][j]

print(matrix[-1][-1])
