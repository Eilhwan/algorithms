# import sys
# read = sys.stdin.readline
# a = list(map(int, read().split()))
# a.sort()
# b = " ".join(list(map(str, a)))
# print(b.rstrip())

print(*sorted(map(int, input().split())), sep=" ")
