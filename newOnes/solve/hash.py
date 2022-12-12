import math

l = int(input())
s = list(input().lower())

for i in range(len(s)):
    s[i] = ord(s[i]) - ord('a') + 1

r = 31
m = 1234567891

_sum = 0
for i, c in enumerate(s):
    _sum += int(c) * (r ** i)

print(_sum % m)

