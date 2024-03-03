
n, m = 6, 4
inp = [[1, 4], [2, 3], [2, 4], [5, 6]]

def find(parent, x):
    if parent[x] != x:
        return find(parent, parent[x])
    return x

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(n + 1)]

for i in range(len(inp)):
    a, b = inp[i]
    union(parent, a, b)
for i in range(1, len(parent)):
    print(find(parent, i), end=" ")

print(parent)