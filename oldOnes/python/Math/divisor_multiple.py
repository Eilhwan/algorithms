# 최대 공약수, 최소 공배수 찾기 6, 9 {1, 2, 3, 6} {1, 3, 9}
a, b = map(int, input().split())


def common(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a


def multiple(a, b):
    return (a * b) // common(a, b)


print(common(a, b))
print(multiple(a, b))
