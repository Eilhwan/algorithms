from collections import deque

n, m = map(int, input().split())
to_pop = list(map(int, input().split()))
a = deque(range(1, n + 1))

answer = 0
for i in range(m):
    pop_index = a.index(to_pop[i])
    length = len(a)
    if pop_index == 0:
        a.popleft()
    elif length // 2 >= pop_index:
        a.rotate(-pop_index)
        answer += abs(-pop_index)
        a.popleft()
    else:
        a.rotate(length - pop_index)
        answer += abs(length - pop_index)
        a.popleft()
print(answer)
