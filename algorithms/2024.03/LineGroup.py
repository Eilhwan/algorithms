import sys

# 두 선분의 교차 여부 판별
def ccw(p1, p2, p3):
    op = (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if op > 0:
        return 1
    elif op < 0:
        return -1
    else:
        return 0

def intersect(line1, line2):
    p1, p2 = line1
    p3, p4 = line2
    ab = ccw(p1, p2, p3) * ccw(p1, p2, p4)
    cd = ccw(p3, p4, p1) * ccw(p3, p4, p2)
    if ab == 0 and cd == 0:
        if p1 > p2:
            p1, p2 = p2, p1
        if p3 > p4:
            p3, p4 = p4, p3
        return p1 <= p4 and p3 <= p2
    return ab <= 0 and cd <= 0

# Union-Find 알고리즘
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 입력
n = int(input())
lines = []
parent = [i for i in range(n)]

for i in range(n):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    lines.append(((x1, y1), (x2, y2)))

# 각 선분들에 대해 교차 여부 확인 후 Union-Find
for i in range(n):
    for j in range(i + 1, n):
        if intersect(lines[i], lines[j]):
            union_parent(parent, i, j)

# 그룹 찾기
groups = {}
for i in range(n):
    root = find_parent(parent, i)
    if root not in groups:
        groups[root] = 1
    else:
        groups[root] += 1

# 출력
print(len(groups))
print(max(groups.values()))
