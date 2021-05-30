import sys; read = sys.stdin.readline

n = int(read())

names = []
for i in range(n):
    names.append(read())
name = names[0]
for i in range(1, len(names)):
    for j in range(len(names[i])):
        if name[j] != names[i][j] and name[j] != "?":
            name = name[:j] + "?" + name[j + 1:]

print(name)
