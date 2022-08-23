


n, k = map(int, input().split())
students = [[0 for _ in range(6)] for _ in range(2)]

for i in range(n):
    s, y = map(int, input().split())
    students[s][y - 1] += 1

ans = 0
for gender in students:
    for classes in gender:
        div, mod = divmod(classes, k)
        if mod > 0:
            div += 1
        ans += div

print(ans)