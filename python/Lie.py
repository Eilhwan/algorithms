import sys

withness = set()

n, m = map(int, sys.stdin.readline().split())

k = list(map(int, sys.stdin.readline().split()))
parties = []
graph = [[] for _ in range(51)]
for i in range(m):
    parties.append(list(map(int, input().split())))

for i in range(m):
    party = parties[i][1:]
    for i in range(1, len(party)):
        graph[i].extend(party)

if k[0] == 0:
    print(0)
else:
    print(graph)