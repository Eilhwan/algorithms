import sys

N = int(sys.stdin.readline())
li = []
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    li.append([x, y])

ans = []
for i in range(N):
    level = 1
    for j in range(N):
        if i != j:
            if li[i][0] < li[j][0] and li[i][1] < li[j][1]:
                level += 1
    ans.append(level)

print(str(ans).lstrip('[').rstrip(']').replace(',', ''))

# res = [0 for _ in range(len(ans))]
# rank = 1

# for i in range(len(ans)):
#     max_value = max(ans)
#     if max_value < 0:
#         break
#     num = 0
#     for j in range(len(ans)):
#         if ans[j] == max_value:
#             res[j] = rank
#             ans[j] = -1
#             num += 1
#     rank += num

# print(str(res).lstrip('[').rstrip(']').replace(',', ''))
