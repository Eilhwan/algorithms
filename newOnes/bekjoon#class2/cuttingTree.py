import sys


N, M = map(int, sys.stdin.readline().split())

li = list(map(int, sys.stdin.readline().split()))

left = 0
right = max(li)
ans = 0
while left <= right :
    middle = (left + right) // 2
    _sum = 0
    for i in range(len(li)):
        if li[i] - middle > 0:
            _sum += li[i] - middle
    
    if _sum >= M:
        ans = max(middle, ans)
        left = middle + 1
    else:
        right = middle - 1
print(ans)