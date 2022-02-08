from collections import deque
import sys
sys.setrecursionlimit(int(10e7))

ans = 0


def dfs(cur, sheeps, wolves, info, graph, dec):
    global ans

    if info[cur] == 0:
        sheeps += 1
    else:
        wolves += 1

    if sheeps <= wolves:
        ans = max(ans, sheeps)
        print(ans)

    else:
        p, l, r = graph[info[cur]]
        if l > -1 and l not in dec:
            dec.append(l)
        if r > -1 and r not in dec:
            dec.append(r)

        index = len(dec)
        for _ in range(index):
            t = dec.pop()
            dfs(t, sheeps, wolves, info, graph, dec)
            dec.appendleft(t)


def solution(info, edges):
    global ans

    graph = [[-1, -1, -1] for _ in range(len(info))]

    for e in edges:
        head = e[0]
        child = e[1]
        graph[child][0] = head
        if graph[head][1] > -1:
            graph[head][1] = min(graph[head][1], child)
            graph[head][2] = max(graph[head][1], child)
        else:
            graph[head][1] = child

    dfs(0, 0, 0, info, graph, deque())
    print(ans)
    return ans


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [
    9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]

solution(info, edges)
