import sys; read = sys.stdin.readline

n, k = map(int, read().split())
dp = [100000 for _ in range(100001)]
dp[0] = 1
coins = []
for i in range(n):
    coins.append(int(read()))
for c in coins:
    dp[c] += 1
for i in range(1, k + 1):
    for coin in coins:
        if i - coin >= 0:
            dp[i] = min(dp[i - coin] + 1, dp[i])
if dp[k] != 100000:
    print(dp[k] - 1)
else:
    print(-1)