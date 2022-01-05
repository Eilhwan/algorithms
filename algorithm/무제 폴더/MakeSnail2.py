n = 10
index = 1
jump = 2

mat = [[0 for _ in range(n)] for _ in range(n)]
direction = 1


jumpStack = 1

while index <= n * n:
    x = 0
    y = -1
    # size 초기화
    size = n

    while size >= 0:
        for _ in range(size):
            y += 1 * direction
            jumpStack -= 1
            if jumpStack == 0:
                if mat[x][y] == 0:
                    mat[x][y] = index
                    index += 1
                jumpStack = jump

        size -= 1

        for _ in range(size):
            x += 1 * direction
            jumpStack -= 1
            if jumpStack == 0:
                if mat[x][y] == 0:
                    mat[x][y] = index
                    index += 1
                jumpStack = jump

        direction = -direction


for line in mat:
    for att in line:
        print(att, end=" ")
    print()
