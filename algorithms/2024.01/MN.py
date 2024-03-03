# 3 1
# 4 5 2

n, m = map(int, input().split())
li = list(map(int, input().split()))

answer = []
def recursive(depth, now):
    if depth == m:
        answer.append(now)
        return
    
    for i in range()