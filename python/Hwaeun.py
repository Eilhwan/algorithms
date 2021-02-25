import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dic = dict()
arr = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if len(a) >= m:
        if dic.__contains__(a):
            dic[a] += 1
        else:
            dic[a] = 1
            arr.append(a)

arr.sort()
arr.sort(key = lambda x: (-dic[x], -len(x), x))
for word in arr:
    print(word)





