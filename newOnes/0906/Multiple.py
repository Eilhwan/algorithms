import sys


def recursive(number, times, c):

    if times == 1:
        return number % c
    
    res = recursive(number, times/2, c) % c
    res = res * res
    if times % 2 == 1:
        return res * res % c * number % c

    return res * res % c

a, b, c = map(int, sys.stdin.readline().split())



res = recursive(a, b, c)

print(res % c)

