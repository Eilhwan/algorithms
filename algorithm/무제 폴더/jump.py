def solution(n, jump):
    answer = [[0 for _ in range(n)] for _ in range(n)]
    number = 1
    x = 0
    y = 0
    step = jump
    size = n
    answer[0][0] = 1

    while n * n >= number:
        if size < 1:  # 출력할 게 없으면 종료
            size = n
            x = 0
            y = 0

        while x < size:
            x += jump
            if 0 <= x < size:
                answer[y][x] = number
                number += 1
        size -= 1

        while y < size:
            y += step
            if 0 <= y < size:
                answer[y][x] = number
                number += 1
        y = size - 1
        step = -step  # 증감 방향을 반대로

    # 2차원 리스트 출력하기
    for line in answer:
        for n in line:
            print('%3d' % n, end='')
        print()

    return [x, y]


n = 5
jump = 3
solution(n, jump)
