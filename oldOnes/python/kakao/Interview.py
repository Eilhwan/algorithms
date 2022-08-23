# 1번 4방향으로 2번 움직였을 때 사람이 있는가?

# 가는 길목에 파티션이 있냐?

def manhathon(p, places):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]  
    x = p[0]
    y = p[1]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if places[nx][ny] == "P":
                return False
            
            for j in range(4):
                # 4면중 오리지널 x를 제외
                if dx[i] + dx[j] != 0 and dy[i] + dy[j] != 0:
                    nx2 = nx + dx[j]
                    ny2 = ny + dy[j]
                    if 0 <= nx2 < 5 and 0 <= ny2 < 5 and places[nx2][ny2] == "P":
                        x_dist = x - nx2
                        y_dist = y - ny2
                        if abs(x_dist) == 2 or abs(y_dist) == 2:
                            if  places[nx][ny] != "X":
                                return False
                        if abs(x_dist) == 1 and abs(y_dist) == 1:
                            if places[x][ny2] != "X" and places[nx2][y] != "X":
                                return False
    return True



def solution(places):
    res = []
    for i in range(5):
        flag = True
        for j in range(5):
            for k in range(5):
                if places[i][j][k] == "P":
                    flag = manhathon([j, k], places[i])
                    if not flag:
                        res.append(0)
                        break
            if not flag:
                break
        if flag:
            res.append(1)
    return res



places=[["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))
# ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"]