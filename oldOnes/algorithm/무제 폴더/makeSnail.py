
n = 1000
index = 1
mat = [[0 for _ in range(n)] for _ in range(n)]
direction = 1

# size 초기화
size = n

x = 0
y = -1

while n * n >= index:
    for _ in range(size):
        y += 1 * direction
        mat[x][y] = index
        index += 1

    size -= 1

    for _ in range(size):
        x += 1 * direction
        mat[x][y] = index
        index += 1

    direction = -direction


for line in mat:
    for att in line:
        print(att, end=" ")
    print()
