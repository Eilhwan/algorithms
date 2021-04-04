import sys

read = sys.stdin.readline
while True:
    n = input()
    if n == "0":
        break
    p1 = 0
    p2 = len(n) - 1
    while p1 < p2:
        if n[p1] != n[p2]:
            print("no")
            break
        p1 += 1
        p2 -= 1

    if n[p1] == n[p2]:
        print("yes")