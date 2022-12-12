from sys import stdin

N, M, B = map(int, stdin.readline().split())

lst = []
for i in range(N):
    lst.append(list(map(int, stdin.readline().split())))

dic = dict()
for arr in lst:
    for i in arr:
        if dic.get(i) is None:
            dic[i] = 1
        else:
            dic[i] += 1

items = dic.items()
blocks = [B for _ in range(257)]
ans = [0 for _ in range(257)]
for i in range(257):
    for key, value in items:
        if key > i:
            ans[i] += ((key - i) * 2) * value
            blocks[i] += (key - i) * value
        else:
            ans[i] += (i - key) * value
            blocks[i] -= (i - key) * value

res = [10e9, 0]
for i in range(257):
    if blocks[i] > -1 and res[0] >= ans[i]:
        res[0] = ans[i]
        res[1] = i

print(res[0], res[1])