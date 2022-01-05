import heapq
from collections import deque
def solution(jobs):
    # 요청 시각(초) | 걸리는 시간(초) | 분류 번호 | 중요도
    heap = []
    jobs = deque(jobs)
    answer = []
    
    # 첫 번째 job
    j = jobs.popleft()
    time = j[0]
    heapq.heappush(heap, [j[3], [j[1], j[2]]])

    while heap:
        job = heapq.heappop(heap)
        time += job[1][0]
        dic = dict()
        answer.append(job[1][1])
        while jobs:
            while heap:
                heap_temp = heapq.heappop(heap)
                dic[heap_temp[1][1]] = [heap_temp[0], heap_temp[1][0]] 
            if jobs[0][0] <= time:
                j = jobs.popleft()
                if j[2] in dic:
                    dic[j[2]] = [dic[j[2]][0] + j[1], dic[j[2]][1] + j[3]]
                else:
                    dic[j[2]] = [j[1], j[3]]
            else:
                break
        
        for key, value in dic.items():
            heapq.heappush(heap, [value[1], [value[0], key]])

    return answer
        
       
        
        
        
        
                
        
        
        
        
        
        
solution([[1, 5, 2, 3], [2, 2, 3, 2], [3, 1, 3, 3], [5, 2, 1, 5], [7, 1, 1, 1], [9, 1, 1, 1], [10, 2, 2, 9]])