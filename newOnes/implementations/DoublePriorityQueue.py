from heapq import heappush, heappop, nlargest
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    k = int(sys.stdin.readline())
    max_heap = []
    min_heap = []
    visited = [False for _ in range(1000001)]
    
    for i in range(k):
        opCode, num = sys.stdin.readline().split()

        if opCode == "I":
            visited[i] = True
            heappush(max_heap, (-int(num), i))
            heappush(min_heap, (int(num), i))
        else:
            if num == "1":
                while max_heap and not visited[max_heap[0][1]]:
                    heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heappop(max_heap)
                    
            else:
                while min_heap and not visited[min_heap[0][1]]:
                    heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heappop(min_heap)
                    
    while max_heap and not visited[max_heap[0][1]]: heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]: heappop(min_heap)
    print(f'{-max_heap[0][0]} {min_heap[0][0]}' if max_heap and min_heap else'EMPTY')