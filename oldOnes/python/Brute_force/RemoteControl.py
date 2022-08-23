N = int(input())
M = int(input())

buttons = [1 for _ in range(10)]
if len(M) > 0:
    arr = list(map(int, input().split()))
    for i in arr:
        buttons[i] = -1

ans = abs(N - 100)

for i in range(500001):
    isPossible = True
    for j in str(i):
        if buttons[int(j)] == -1:
            isPossible = False
            break
    if isPossible:
        ans = min(len(str(i)) + abs(N - i), ans)

print(ans)
