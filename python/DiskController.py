import heapq

def solution(jobs):
    time, answer, heap = 0, 0, []
    for i in range(len(jobs)):
        heapq.heappush(heap, [jobs[i][0], jobs[i]])

    
    while heap:
        work = heapq.heappop(heap)
        if work[1][0] > time:
            time = work[1][0]
        print(time)
        answer += time - work[1][0] + work[1][1]
        time += work[1][1]
        
        for i in range(len(heap)):
            heap[i][0] = time - heap[i][1][0] + heap[i][1][1]
        heapq.heapify(heap)
    
    return int(answer / len(jobs))