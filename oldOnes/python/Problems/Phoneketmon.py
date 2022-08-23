def solution(nums):
    return min(len(nums) // 2, len(set(nums)))

numss = [[3,1,2,3],	
[3,3,3,2,2,4],
[3,3,3,2,2,2]]

for i in numss:
    print(solution(i))