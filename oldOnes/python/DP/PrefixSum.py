# N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.

# 예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.

# 1	2	3	4
# 2	3	4	5
# 3	4	5	6
# 4	5	6	7
# 여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.

# 표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.

import sys
read = sys.stdin.readline

N, M = map(int, read().strip().split())

table = [[0 for _ in range(N+1)]]
psum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(N):
    table.append([0] + list(map(int, read().strip().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        psum[i][j] = psum[i][j-1] + psum[i-1][j] - psum[i-1][j-1] + table[i][j]


for i in range(M):
    x1, y1, x2, y2 = map(int, read().split())

    print(psum[x2][y2] - psum[x2][y1-1] - psum[x1-1][y2] + psum[x1-1][y1-1])
