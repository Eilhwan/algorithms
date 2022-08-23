
K, N = map(int, input().split())

table = list()
for _ in range(K):
    table.append(int(input()))


# 어떤걸 탐색할 거냐
start = 0
end = max(table)
ans = 0

while end >= start:
    mid = (end + start) // 2 if (end + start) // 2 else 1
    # 탐색을 하는 부분 => 식은 어떻게 되느냐
    temp = sum(map(lambda x: x // mid, table))
    if temp >= N:
        if ans < mid:
            ans = mid
        start = mid + 1
    else:
        end = mid - 1


print(ans)
