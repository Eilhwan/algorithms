# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
from collections import Counter
import sys


readline = sys.stdin.readline

N = int(input())
li = Counter(list(map(int, readline().split())))
M = int(input())
ca = list(map(int, readline().split()))
ans = ""

for i in range(len(ca)):
    if li.get(ca[i]) is not None:
        ans  += str(li.get(ca[i])) + " "
    else:
        ans += "0 "
print(ans.strip())