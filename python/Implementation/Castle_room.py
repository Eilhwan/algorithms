import sys; read = sys.stdin.readline
# 7 4
# 11 6 11 6 3 10 6
# 7 9 6 13 5 15 5
# 1 10 12 7 13 7 5
# 13 11 10 8 10 12 13

n, m = map(int, input().split())

castle = []
for i in range(m):
    castle.append(list(map(int, read().strip().split())))

visited = [[False for _ in range(n)] for _ in range(m)]
bit_array = [1, 2, 4, 8]
room_cnt = 0
room_width = 0
def calculate_room(i, j):
    global room_width
    temp_room_width = 0
    if not visited[i][j]:
        visited[i][j] = True
        for k in range(len(bit_array)):
            if not bit_array[k] & castle[i][j]:
                # go.. k == 0, k == 1 ...

                calculate_room()
                room_width += 1


    
    room_width = room_width

        

# Bitmasking에 대한 정보 서 1 북 2 동 4 남 8 15 == 사방이 막혀있다.
# 0001 서
# 0010 북
# 0100 동
# 1000 남



