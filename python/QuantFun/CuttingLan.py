
K, M = map(int, input().split())

table = []
for _ in range(K):
    table.append(int(input()))


start = 0
end = max(table)
ans = 0

while end >= start:
    mid = (end + start) // 2 and (end + start) // 2 or 1
    temp = sum(map(lambda x: x // mid, table))
    if temp >= M:
        if ans < mid:
            ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
