n = int(input())
k = 0
while True:
    bn = bin(n+1)
    if bn.count("1") == 1:
        print(len(bn)-3)
        break
    n = n >> 1
