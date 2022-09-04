from math import factorial

# 5 2
n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))