n = int(input())
vec = list(map(int, input().split()))
v = int(input())

res = 0
for i in vec:
    if i == v:
        res += 1
print(res)