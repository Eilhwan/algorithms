
T = int(input())


def dp(start, end):
    if dpTable[start][end] != -1:
        return dpTable[start][end]

    if start == end:
        return 0

    ans = float("inf")
    s = sum(pages[start: end+1])
    for i in range(start, end):
        temp = dp(start, i) + dp(i + 1, end) + s

        if ans > temp:
            ans = temp

    return ans


for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))

    dpTable = [[-1] * (K + 1) for i in range(K + 1)]

    print(dp(0, K-1))
