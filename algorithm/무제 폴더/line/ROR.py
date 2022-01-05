from collections import deque


def solution(maps):
    maps_cLen = len(maps)
    maps_rLen = len(maps[0])
    # start = 0, 0
    # end = 4, 4

    dcol, drow = [1, -1, 0, 0], [0, 0, 1, -1]
    dist = [[-1 for _ in range(maps_rLen)] for _ in range(maps_cLen)]
    dist[0][0] = 1
    q = deque([(0, 0)])
    while q:
        cCol, cRow = q.popleft()
        for i in range(4):
            ncol = cCol + dcol[i]
            nrow = cRow + drow[i]
            if 0 <= ncol < maps_cLen and 0 <= nrow < maps_rLen:
                if maps[ncol][nrow] == 1 and dist[ncol][nrow] == -1:
                    dist[ncol][nrow] = dist[cCol][cRow] + 1
                    q.append([ncol, nrow])

    return dist[-1][-1]


maps = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]

print(solution(maps))
