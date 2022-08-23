from collections import deque

def findMin(que, min_value):
    
    for i in range(len(que)):
        if min_value < que[i][1]:
            return False
    return True

T = int(input())

for _ in range(T):
    # M 번째 수는 언제 출력 되나
    N, M = map(int, input().split())

    priority = list(map(int, input().split()))
    li = []

    for i in range(N):
        li.append([i, priority[i]])
    q = deque(li)
    index = 1
    while q:
        min_value = q.popleft()
        if findMin(q, min_value[1]):
            if min_value[0] == M:
                print(index)
            index += 1
        else:
            q.append(min_value)
    

        