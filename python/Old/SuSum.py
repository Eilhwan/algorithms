import sys

n = int(sys.stdin.readline())

for i in range(n):
    print("#", i + 1, end=" ")
    temp = list(map(int, (sys.stdin.readline().split())))
    ans = 0
    for j in temp:
        if j % 2 != 0:
            ans += j
    print(ans)

    f"{ans}"