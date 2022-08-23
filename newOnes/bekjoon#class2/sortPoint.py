# 5
# 0 4
# 1 2
# 1 -1
# 2 2
# 3 3

n = int(input())
li = []
for _ in range(n):
    x, y = map(int, input().split())
    li.append([x, y])

for x, y in sorted(li, key=lambda x: (x[1], x[0])):
    print(x, y)
