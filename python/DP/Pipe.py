import sys; read = sys.stdin.readline

# result = 0
# def find_route(start, prev):
#     global result
#     a, b = start
#     if a == (n - 1) and b == (n - 1):
#         result += 1
#         return
#     for i in range(3):
#         x = a + matrix[i][0]
#         y = b + matrix[i][1]
#         if (i == 0 and prev == 1) or (i == 1 and prev == 0):
#             continue
#         if x >= n or y >= n or room[x][y] == 1 or room[x][y] == 1:
#             continue
#         if i == 2 and (room[x][y - 1] == 1 or room[x - 1][y] == 1):
#             continue

#         find_route([x, y], i)
        
    

n = int(read())
matrix = [[0, 1], [1, 0], [1, 1]]
room = []
dp = []
for _ in range(n):
    room.append(list(map(int, read().split())))

x = 0
y = 1
prev  = 0
# find_route(start, prev)
res = 0
while True:
    
    for i in range(3):
        x += matrix[i][0]
        y += matrix[i][1]
print(res)

