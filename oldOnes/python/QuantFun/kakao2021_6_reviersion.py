
from glob import glob


l = [-1] * 20
r = [-1] * 20

val = []
n = 0
ans = 1
vis = [0] * (1 << 17)


def solve(state):
    global ans
    if vis[state]:
        return None
    vis[state] = 1
    wolf, num = 0, 0
    for i in range(n):
        if state & (1 << i):
            num += 1
            wolf += val[i]
    if 2 * wolf >= num:
        return None
    ans = max(ans, num - wolf)

    for i in range(n):
        if not state & (1 << i):
            continue
        if l[i] != -1:
            solve(state | (1 << l[i]))
        if r[i] != -1:
            solve(state | (1 << r[i]))


def solution(info, edges):
    global n, val
    n = len(info)
    val = info[:]
    for u, v in edges:
        if l[u] == -1:
            l[u] = v
        else:
            r[u] = v

    solve(1)
    return ans
