import itertools as it
from heapq import heappush, heappop, heapify, heappushpop, heapreplace
from bisect import bisect_left, bisect_right
from collections import Counter

arr = ["A", "B", "C", "D"]

print(list(it.combinations(arr, 3)))
print(list(it.permutations(arr, 3)))
print(list(it.product(arr, repeat=1)))
print(list(it.combinations_with_replacement(arr, 2)))

#################################
#                               #
#             heap              #
#                               #
#################################

print(heapify(arr))
