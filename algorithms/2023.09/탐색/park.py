def solution(park, routes):
    # 시작위치 정하기
    x, y = -1, -1
    for i in range(len(park)):
        for j in range(len(park[0])):
            if "S" == park[i][j]:
                x, y = i, j
                break
        if x != -1:
            break
    #Route에 있는 변수 반복
    for r in routes:
        d, l = r.split()
        dx, dy = x, y
        l = int(l)
        
        if d == "E":
            dy += l
        elif d == "W":
            dy -= l
        elif d == "N":
            dx -= l
        elif d == "S":
            dx += l

        # 이동한 목표가 밖으로 나가지 않으면서
        if 0 <= dx < len(park) and 0 <= dy < len(park[0]):
            p = True
            # 가는 길에 X가 있는 지 확인
            for i in range(x+1, dx+1):
                if park[i][dy] == "X":
                    p = False
                    break
            for j in range(y+1, dy+1):
                if park[dx][j] == "X":
                    p = False
                    break
            if p:
                x, y = dx, dy
        
    return [x,y]