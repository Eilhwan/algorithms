
a= 1
for i in range(3):
    a *= (int(input()))

c = [0 for _ in range(10)]
for i in range(10):
    print(str(a).count(str(i)))
