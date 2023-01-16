
# 10
# 1 5 2 1 4 3 4 5 2 1
n = int(input())
sq1 = [0] + list(map(int, input().split()))
sq2 = sq1[1:] + [0]
dp1 = [0 for _ in range(len(sq1))] # 올라가는 수열
dp2 = [0 for _ in range(len(sq2))] # 내려가는 수열
max1 = 0
for i in range(1, len(sq1)):
    for j in range(i):
        if sq1[i] > sq1[j]:
            dp1[i] = max(dp1[j]+1, dp1[i])
            

for i in range(len(sq2)):
    for j in range(i):
        if sq2[i] < sq2[j]:
            dp2[i] = max(dp2[j]+1, dp2[i])

print(max1)
print(dp1)