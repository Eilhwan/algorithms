n = int(input())
sq = list(map(int, input().split())) + [0]
dp = [0 for _ in range(len(sq))]

for i in range(len(sq)):
    for j in range(i):
        if sq[i] < sq[j]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))