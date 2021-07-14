def check_distance(x, y, place):
    dx = [1, 0, 0, -1]
    dy = [0, 1, -1, 0]
    n = len(place)
    m = len(place[0])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if place[nx][ny] == "P":
                return False
            elif place[nx][ny] == "O":
                if 0 <= nx + dx[i] < n and 0 <= ny + dy[i] < m and place[nx + dx[i]][ny + dy[i]] == "P":
                    return False


    dx2 = [-1, -1, 1, 1]
    dy2 = [-1, 1, -1, 1]
    for i in range(4):
        nx = x + dx2[i]
        ny = y + dy2[i]
        if 0 <= nx < n and 0 <= ny < m:
            if place[nx][ny] == "P":
                if not (place[nx][y] == "X" and place[x][ny] == "X"):
                    return False

        
    return True

def solution(places):
    answer = []
    for p in places:
        place = []
        for cl in p:
            place.append(list(cl))
        # P = Person O = empty table X = Partition
        is_safty = True
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == "P":
                    is_safty = check_distance(i, j, place)
                if not is_safty:
                    break
            if not is_safty:
                break
        if is_safty:
            answer.append(1)
        else:
            answer.append(0)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]

print(solution(places))