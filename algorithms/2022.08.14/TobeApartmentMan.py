T = int(input())

for _ in range(T):
    K = int(input())
    N = int(input())

    apart = [[i for i in range(N+1)]]

    for i in range(1, K + 1):
        stair = []
        for j in range(N):
            stair.append(sum(apart[-1][:j+1]))
        apart.append(stair)

    print(apart[-1][-1])