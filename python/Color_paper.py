
n = int(input())
table = []
for i in range(n):
    table.append(list(map(int, input().split())))
vistied = [[False for _ in range(n)] for _ in range(n)]

blue = 0
white = 0

def recursive(r, c, n):
    global white, blue
    temp = table[r][c]
    for i in range(r, r + n):
        for j in range(c, c + n):
            if temp != table[i][j]:
                recursive(r, c, n // 2)
                recursive(r, c + n // 2, n // 2)
                recursive(r + n // 2, c, n // 2)
                recursive(r + n // 2, c + n // 2, n // 2)
                return

        if temp == 0:
            white += 1
            return
        else:
            blue += 1
            return



recursive(0, 0, n)
print(white)
print(blue)