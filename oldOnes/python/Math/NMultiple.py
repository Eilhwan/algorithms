from math import lcm
from math import gcd


def common(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def multiple(a, b):

    return (a * b) // common(a, b)


def solution(arr):
    answer = 0
    while len(arr) > 1:
        temp = []
        for i in range(len(arr) - 1):
            temp.append(multiple(arr[i], arr[i+1]))
        arr = temp

    return arr[0]


print(lcm(1, 2, 3, 4, 9))
