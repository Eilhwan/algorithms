from math import factorial
n = int(input())
cnt = 0
for c in str(factorial(n))[::-1]:
    if c == '0':
        cnt += 1
    else:
        break

print(cnt)