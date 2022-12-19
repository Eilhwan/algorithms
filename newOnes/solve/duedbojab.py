n, m = map(int, input().split())

db = [input() for _ in range(n)]
bb = []
for i in range(m):
    name = input()
    if name in db:
        bb.append(name)
print(len(bb))
for name in sorted(bb):
    print(name) 
