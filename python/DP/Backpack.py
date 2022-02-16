import sys
read = sys.stdin.readline

# N(1 ≤ N ≤ 100)과 준서가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)
N, K = map(int, read().rstrip().split())

# 두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와 해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
things = [list(map(int, read().rstrip().split())) for _ in range(N)]
things.sort(key=lambda x: x[0])

dp = [0 for _ in range(K+1)]

for weight, value in things:
    for j in range(K, weight-1, -1):
        dp[j] = max(dp[j], dp[j-weight] + value)


print(dp[-1])
