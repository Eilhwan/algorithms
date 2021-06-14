

arr = [0 for _ in range(10001)]


for i in range(1, 10001):
    a = i
    for j in range(len(str(i))):
        a += int(str(i)[j])
    if a <= 10000:
        arr[a] += 1

for i in range(1, len(arr)):
    if arr[i] == 0:
        print(i)
