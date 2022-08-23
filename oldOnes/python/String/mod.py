c = []
for _ in range(10):
    temp = int(input()) % 42
    if temp not in c:
        c.append(temp % 42)
print(len(c))
    