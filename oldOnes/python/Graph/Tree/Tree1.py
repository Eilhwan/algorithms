# 2
# 4
# 3 2 1 4
# 2 3 4 1
# 8
# 3 6 5 4 8 7 1 2
# 5 6 8 4 3 1 2 7
def find(s, e):
    if s > e:
        return
    num = preOrder[preIdx]
    preIdx += 1
    inIndex = -1
    for i in range(s, e+1):
        if inOrder[i] == num:
            inIndex += 1
            break
    find(s, inIndex - 1)
    find(inIndex + 1, e)
    res += num


T = int(input())
for _ in range(T):
    n = int(input())
    preOrder = list(input().split())
    inOrder = list(input().split())

    pre_now = prOrder[0]
    index = 0

    find()
