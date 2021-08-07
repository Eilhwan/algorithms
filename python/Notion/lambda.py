

def filter(func, arr):
    temp = []
    for a in arr:
        temp.append(func(a))
    return temp


res = filter(lambda x: -x, [1, 2, -3])
print(res)
