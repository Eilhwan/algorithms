import sys;input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
s = int(input())


while s > 0:
    tmp_cnt = s
    now_max = 0
    for i in range(len(numbers)):
        if numbers[now_max] < numbers[i]:
            now_max = i
        
    

