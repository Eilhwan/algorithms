n = int(input())
s = 0
for _ in range(n):
    c = input().split()
    i = 0
    if len(c) > 1:
        i = int(c[1])
    c = c[0]

    if c == "add":
        s = s | pow(2, i)
    elif c == "check":
        if s & pow(2, i) != 0:
            print(1)
        else:
            print(0)
    elif c == "remove":
        s = s & (pow(2, i) - (1 ^ pow(2, i)))
    elif c == "toggle":
        if s & i:
            s = s & (2**21 - 1 ^ 2**i)
        else:
            s = s | 2**i
    elif c == "all":
        s = 2**21 - 1
    elif c == "empty":
        s = 0
    
