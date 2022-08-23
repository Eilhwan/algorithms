from heapq import heapify, heappop, heappush
# from queue import PriorityQueue
# n = int(input())
# q = PriorityQueue()
# for i in range(n):
#     q.put(int(input()))

# ans = 0
# for i in range(n - 1):
#     a = q.get()
#     b = q.get()
#     temp = a + b
#     q.put(temp)
#     ans += temp

# print(ans)

n = int(input())
heap = []
for i in range(n):
    heappush(heap, int(input()))

ans = 0
for i in range(n - 1):
    temp = heappop(heap) + heappop(heap)
    ans += temp
    heappush(heap, temp)
print(ans)


