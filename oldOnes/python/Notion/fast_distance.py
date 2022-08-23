import sys; read = sys.stdin.readline
import heapq

n, d = map(int, read().rstrip())

graph = [[] for _ in range(n)]
distance = [10e9 for _ in range(d)]

for i in range(n):
    start, end, cost = map(int, read().rstrip())
    
