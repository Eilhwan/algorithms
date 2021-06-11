import sys; read = sys.stdin.readline
def diffuse():
    global arr
    global arr2
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] > 4:
                # diffuse
                pie = arr[i][j] // 5
                cnt = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < len(arr) and 0 <= y < len(arr[0]) and arr[x][y] != -1:
                        arr2[x][y] += pie
                        cnt += 1
                arr[i][j] -= pie * cnt
    
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] != -1:
                arr[i][j] += arr2[i][j]

def clean(cleaner):
    global arr
    _up = cleaner[0]
    _down = cleaner[1]
    _down[1] += 1
    _up[1] += 1
    temp = 0
    # 1 = y 
    while _down[1] < len(arr[0]):
        temp, arr[_down[0]][_down[1]] = arr[_down[0]][_down[1]], temp
        _down[1] += 1
    _down[0] += 1
    _down[1] -= 1
    while _down[0] < len(arr):
        temp, arr[_down[0]][_down[1]] = arr[_down[0]][_down[1]], temp
        _down[0] += 1
    _down[0] -= 1
    _down[1] -= 1
    while _down[1] >= 0:
        temp, arr[_down[0]][_down[1]] = arr[_down[0]][_down[1]], temp
        _down[1] -= 1
    _down[0] -= 1
    _down[1] += 1
    while _down[0] >= 0:
        if arr[_down[0]][_down[1]] == -1:
            break
        temp, arr[_down[0]][_down[1]] = arr[_down[0]][_down[1]], temp
        _down[0] -= 1
    # 아랫 놈
    temp = 0
    while _up[1] < len(arr[0]):
        temp, arr[_up[0]][_up[1]] = arr[_up[0]][_up[1]], temp
        _up[1] += 1
    _up[0] -= 1
    _up[1] -= 1
    while _up[0] >= 0:
        temp, arr[_up[0]][_up[1]] = arr[_up[0]][_up[1]], temp
        _up[0] -= 1
    _up[0] += 1
    _up[1] -= 1
    while _up[1] >= 0:
        temp, arr[_up[0]][_up[1]] = arr[_up[0]][_up[1]], temp
        _up[1] -= 1
    _up[0] += 1
    _up[1] += 1
    while _up[0] < len(arr):
        if arr[_up[0]][_up[1]] == -1:
            break
        temp, arr[_up[0]][_up[1]] = arr[_up[0]][_up[1]], temp
        _up[0] += 1
    
    
        


r, c, t = map(int, read().split())
arr =  [list(map(int, read().split())) for _ in range(r)]
cleaner = []
for i in range(c):
    if arr[i][0] == -1:
        cleaner = [[i, 0], [i + 1, 0]]
        break

ans = 0

for i in range(t):
    arr2 = [[0 for _ in range(c)] for _ in range(r)]
    diffuse()
    clean(cleaner)

for i in range(len(arr)):
    ans += sum(arr[i])
print(ans + 2)

