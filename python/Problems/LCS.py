

n, k = map(int, input().split())

numbers = list(map(int, input().split()))

max_len = 0
length = 0
a = [0] * (n + 1)
for i in range(len(numbers)):
    a[numbers[i]] += 1
    length += 1
    if a[numbers[i]] > k:
        # a[number[i + 1]] - k 번째 number[i + 1] 한 칸 뒤부터 수를 세야함
        length -= len(numbers[:numbers.index(numbers[i])])
        print(numbers[numbers.index(numbers[i]) + 1:])
    if length > max_len:
        max_len = length

print(max_len)
