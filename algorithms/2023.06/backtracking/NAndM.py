
def backtracking(index, depth, li, res, vistied):
    if len(res) == depth:
        print(' '.join(map(str, res)))
        return

    for i in range(index, len(li)):
        if not vistied[i]:
            vistied[i] = True
            res.append(li[i])
            backtracking(i + 1, depth, li, res, vistied)
            res.pop()
            vistied[i] = False

N, M = map(int, input().split())

li = [i for i in range(1, N+1)]

backtracking(0, M, li, [], [False] * N)

