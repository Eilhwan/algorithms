
N = int(input())

target = 1
room = 1

while target < N:
    target += (6 * room)
    room += 1
            
print(room)
    