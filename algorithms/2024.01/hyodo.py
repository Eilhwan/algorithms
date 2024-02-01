# 4 3
# ABC
# 1 4 A
# 4 2 C
# 3 1 B
def lcs(a, b):
    x = len(a)
    y = len(b)
    mat = [[0 for _ in range(x+1)] for _ in range(y+1)]

    for i in range(x+1):
        for j in range(y+1):
            if i == 0 or j == 0:
                mat[i][j] = 0
            elif a[i-1] == b[j-1]:
                mat[i][j] = mat[i-1][j-1] + 1
            else:
                mat[i][j] = max(mat[i][j-1], mat[i-1][j])
    return mat[x][y]

import sys;input=sys.stdin.readline

n, m = map(int, input().split())
abc = input()

tree = [[] for _ in range(n+1)]
for _ in range(m):
    _from, _to, _alpha = input().split()
    tree[int(_from)].append([int(_to), _alpha])
    tree[int(_to)].append([int(_from), _alpha])

str1 = ""
answer = 0
stack = list()
stack.append(1)
visited = [False] * (n+1)
while stack:
    now = stack.pop()

    for i in range(len(tree[now])):
        next = tree[now][i][0]
        if not visited[i]:
            visited[i] = True
            stack.append(i)
            str1 += tree[now][i][1]
            answer = max(lcs(abc, str1), answer)
            str1 = str1[:-1]

