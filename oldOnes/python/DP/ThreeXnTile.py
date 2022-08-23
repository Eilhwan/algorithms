
def solution(n):
    dp = [0 for _ in range(n + 1)]
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] += dp[i - 2] * 3
        print(dp[i - 2] * 3)
        if i % 2 == 0:
            for j in range(i - 4, -1, -1):
                dp[i] += dp[j] * 2
        dp[i] %= 1000000007
    return dp
    # return dp[n] % 1000000007

print(solution(1000))
