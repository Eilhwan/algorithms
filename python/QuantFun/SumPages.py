
T = int(input())

for _ in range(T):
    K = int(input())
    pages = list(map(int, input().split()))

    dp = [[-1] * (K + 1) for i in range(K + 1)]

    print(dp)
