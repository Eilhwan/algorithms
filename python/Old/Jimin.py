

n, m = map(int, input().split())
list_1 = list(map(int, input().split()))
k, s = list_1[0], set(list_1[1:])
party = []
ans = 0
for i in range(m):
    list_2 = list(map(int, input().split()))
    party.append([list_2[0], list_2[1:]])


for i in range(m):
    if s.intersection(set(party[i][1])):
        s = s.union(set(party[i][1]))
for i in range(m):
    s2 = set(party[i][1])
    if not s2.intersection(s):
        ans += 1
print(ans)    




    