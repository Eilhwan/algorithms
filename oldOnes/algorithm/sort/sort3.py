import sys;read = sys.stdin.readline
n = int(read())
m = [0 for _ in range(10001)]

for i in range(n):
    m[int(read())] += 1

for i in range(len(m)):
    for j in range(m[i]):
        print(i)

input()
sys.stdout.write()