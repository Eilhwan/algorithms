n = int(input())
m = int(input())
answer = 0
mv = int(10e9)
times = 1
while times ** 2 <= m:
    if n <= times ** 2:
        answer += times ** 2
        mv = min(mv, times ** 2)
    times += 1
if answer == 0:
    print(-1)
else:
    print(answer)
    print(mv)