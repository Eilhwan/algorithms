import math
while True:
    a = list(map(int, input().split()))
    if a[0] == a[1] == a[2] and a[0] == 0:
        break
    a.sort()
    if math.sqrt(a[0] ** 2 + a[1] ** 2) == math.sqrt(a[2] ** 2):
        print("right")
    else:
        print("wrong")

