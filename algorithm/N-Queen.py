def check(row):
    for i in range(row):
        if arr[i] == arr[row] or (row - i == abs(arr[row] - arr[i])):
            return False
    return True


def recursive(row):
    global ans
    # 종료
    if row == n:
        ans += 1
        return

    # 재귀
    for i in range(n):
        arr[row] = i
        if check(row):
            recursive(row + 1)


n = int(input())

ans = 0

arr = [-1 for _ in range(n)]

recursive(0)
print(ans)
# 해당 위치가 유효한지...

# 유효하다면 재귀호출...
