from heapq import heapify, heappop, heappush

li = [[1, "A"], [2, "B"], [3, "A"], [7, "B"], [5, "B"], [6,  "C"], [4, "B"]]
heap = []

for i in range(len(li)):
    heappush(heap, li[i])

for i in range(len(heap)):
    print(heappop(heap))
