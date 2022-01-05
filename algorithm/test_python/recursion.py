


def recursion(a, k):
    res.append(a)
    
    for _ in range(a[k]):
        if k < len(a) - 1:
            a[k] -= 1
            a[k + 1] += 1
            recursion(a, k + 1)

res = list()
for i in range(3):
    a = [0, 0, 0, 0]
    a[i] = 4
    recursion(a, i)

print(res)