import sys;input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
s = int(input())
index = 0
while s > 0:
    if index == len(numbers):
        break
    tmp_s = 0
    max_index = index
    max_value = numbers[max_index]
    for i in range(max_index+1, len(numbers)):
        if s == tmp_s or (i - index) > s:
            break
        if numbers[max_index] < numbers[i]:
            max_index = i
            max_value = numbers[max_index]
            tmp_s = i - index
    
    for i in range(max_index, index, -1):
        numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
    s -= tmp_s
    index += 1
for i in numbers:
    print(i, end=" ")

        
    

