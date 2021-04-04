


n, k = map(int, input().split())

numbers = list(map(int, input().split()))
p1 = 0
p2 = 0

while p1 < n:
    p1 += 1
    while p2 < p1 and p1 < n:
        numbers[p2: p1 + 1]
        numbers[p1]