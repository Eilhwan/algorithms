from collections import deque

n = int(input())

l = list(map(int, input().split()))
d = deque()
for i, el in  enumerate(l):
    d.append((i + 1, el))

order = []
for i in range(n):
    popped = d[0]
    d.rotate(-popped[1])
    order.append(popped[0])
    d.remove(popped)


for i in order:
    print(i, end=" ")