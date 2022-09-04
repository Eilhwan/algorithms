# 3
# 21 Junkyu
# 21 Dohyun
# 20 Sunyoung

t = int(input())

li = []
for _ in range(t):
    li.append(list(input().split()))

for i, val in sorted(li, key=lambda x: (int(x[0]))):
    print(i + " " + val)