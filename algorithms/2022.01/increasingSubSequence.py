# 6
# 10 20 10 30 20 50

n  = int(input())
sq = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(i):
        if sq[i] > sq[j]:
            dp[i] = max(dp[j] + 1, dp[i])
            
print(max(dp))