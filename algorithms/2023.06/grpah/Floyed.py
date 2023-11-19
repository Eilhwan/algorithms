import sys;input=sys.stdin.readline
n = int(input())
m = int(input())

cities = [[int(10e9) if i != j else 0 for i in range(n)] for j in range(n)]

for i in range(m):
    a, b, c = map(int, input().split())
    cities[a-1][b-1] = min(c,cities[a-1][b-1])

for k in range(n):
    for a in range(n):
        for b in range(n):
            cities[a][b] = min(cities[a][k] + cities[k][b], cities[a][b])

for i in range(n):
    for j in range(n):
        print(cities[i][j] == int(10e9) if 0 else cities[i][j], end=" ")
    print()

    