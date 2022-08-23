a = input().upper()
c = [0 for _ in range(ord("Z") - ord("A") + 1)]
for i in range(len(a)):
    p = ord(a[i]) - ord("A")
    c[p] += 1
max_value = max(c)
print("?") if c.count(max_value) > 1 else print(chr(c.index(max_value) + 65))

    
