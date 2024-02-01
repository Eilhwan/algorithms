import sys;input=sys.stdin.readline

n = int(input())
answer = ""
for _ in range(n):
    s, t = input().split()
    i = s.lower().find("x")
    answer += t[i].upper()
print(answer)

import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
	inp = input().split()
	index = inp[0].lower().index('x')
	print(inp[1].upper()[index], end='')