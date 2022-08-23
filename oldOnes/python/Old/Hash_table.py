

table = [None for _ in range(10)]
keys = [chr(i) for i in range(ord('a'), ord('z') + 1)]

print(keys)

MAX_INDEX = 10

for key in keys:
    a = hash(key) % MAX_INDEX
    if table[a] == None:
        

print(table)
