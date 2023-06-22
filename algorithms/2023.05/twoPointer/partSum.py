n, s = map(int, input().split())
arr = list(map(int, input().split()))

index = 0
length = 100000
partSum = arr[0]
result = n + 1

for i in range(1, n+1):
    partSum += arr[i]
    while partSum > s:
        length = min(length, i - index)
        partSum -= arr[index]
        index += 1

if length == 100000:
    length = 0

print(length)
