import sys
read = sys.stdin.readline

n, m = map(int, read().strip().split())
arr = list(map(int, read().strip().split()))


def divide(x):
    minX = maxX = arr[0]
    cnt = 1

    for i in range(1, n):
        minX = min(minX, arr[i])
        maxX = max(maxX, arr[i])
        if (maxX - minX) > x:
            cnt += 1
            minX = maxX = arr[i]

    return cnt


left = 0
right = max(arr)

while left <= right:
    mid = right + left // 2
    if divide(mid) <= m:
        right = mid - 1
        result = mid
    else:
        left = mid + 1

print(result)
