# 5 8 3
# 2 4 5 4 6

N, M, K = map(int, input().split())

arr = list(map(int, input().split()))

arr.sort(reverse=True)

# index = 0
# ans = 0

# for i in range(M):
#     if index % K == 0 and index != 0:
#        ans += arr[1]
#     else:
#         ans += arr[0]
#     index += 1

# print(ans)

first = arr[0]
second = arr[1]

count = M - int(M / (K + 1)) * K
count += M % (K + 1)

res = 0
res += count * first
res += (M - count) * second

print(res)