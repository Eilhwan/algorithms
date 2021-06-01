c = [-1 for _ in range(26)]
a = input()
for i in range(len(a)):
    if c[ord(a[i]) - ord('a')] == -1:
        c[ord(a[i]) - ord('a')] = i
for i in c:
    print(i, end=" ")