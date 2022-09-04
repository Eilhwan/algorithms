# level = bronze 2
# https://www.acmicpc.net/problem/10250
# 몸풀기 문제

# 2
# 6 12 10
# 30 50 72
T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    div, mod = divmod(N, H)
    if mod == 0:
        mod = H
    else:
        div += 1
    if div < 10:
        print(f'{mod}0{div}')
    else:
        print(f'{mod}{div}')